# TPU (Tensor Processing Units) - Guida Completa

> Hardware accelerator specializzato per deep learning, gratuito su Kaggle.

---

## Overview

I TPU sono acceleratori hardware specializzati per task di deep learning. Disponibili **gratuitamente** su Kaggle.

### Quota

- **20 ore/settimana** di TPU
- **9 ore massime** per singola sessione
- Supportati in TensorFlow 2.1+ e PyTorch

---

## TPU in Keras/TensorFlow

### Setup Base

```python
import tensorflow as tf

# 1. Rileva e inizializza TPU
tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
tf.tpu.experimental.initialize_tpu_system(tpu)

# 2. Crea strategia di distribuzione
tpu_strategy = tf.distribute.TPUStrategy(tpu)

# 3. Crea modello nello scope della strategia
with tpu_strategy.scope():
    model = tf.keras.Sequential([...])  # definisci modello
    model.compile(...)

# 4. Training normale
model.fit(training_dataset, epochs=EPOCHS, steps_per_epoch=...)
```

---

## Batch Size e Learning Rate

### Regola del Pollice

> **128 elementi per core** = Batch size ottimale

TPU v3-8 ha 8 core, quindi:
```python
BATCH_SIZE = 128 * tpu_strategy.num_replicas_in_sync  # = 1024
```

### Scaling del Learning Rate

Con batch più grandi:
- Aumenta proporzionalmente il learning rate
- Esempio: batch 4x più grande → learning rate 4x più alto
- Richiede tuning per trovare l'ottimo

### steps_per_execution (TF 2.4+)

```python
model.compile(
    ...,
    steps_per_execution=32  # Invia più batch al TPU insieme
)
```

Vantaggi:
- Riduce overhead di comunicazione
- Permette ottimizzazioni XLA cross-batch
- Non servono più batch enormi (>=64 è sufficiente)

---

## tf.data.Dataset e TFRecords

### Best Practice

> Organizza i dati su GCS in **10-100 file** di **10-100 MB ciascuno**

I TPU leggono SOLO da Google Cloud Storage (GCS).

### Caricare TFRecords

```python
# Path su GCS
filenames = tf.io.gfile.glob("gs://bucket/data/*.tfrec")

# Setup ottimizzato
AUTO = tf.data.experimental.AUTOTUNE
ignore_order = tf.data.Options()
ignore_order.experimental_deterministic = False

# Caricamento parallelo
dataset = tf.data.TFRecordDataset(filenames, num_parallel_reads=AUTO)
dataset = dataset.with_options(ignore_order)
dataset = dataset.map(parse_function)  # Decodifica TFRecord
```

### Parametri Chiave

- `num_parallel_reads=AUTO`: Leggi da più file in parallelo
- `experimental_deterministic=False`: Non forzare ordine (più veloce)

---

## Dataset Privati con TPU

Per dataset privati Kaggle con TPU:

```python
# Step 1: Ottieni credenziali
from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
user_credential = user_secrets.get_gcloud_credential()

# Step 2: Imposta credenziali TensorFlow
user_secrets.set_tensorflow_credential(user_credential)

# Step 3: Ottieni path GCS del dataset
from kaggle_datasets import KaggleDatasets
GCS_DS_PATH = KaggleDatasets().get_gcs_path()
```

Per dataset pubblici, basta solo Step 3.

---

## Hardware TPU

### TPU v3-8

| Specifica | Valore |
|-----------|--------|
| Dimensioni | ~50 cm |
| Chip | 4 dual-core (8 core totali) |
| Matrix Multipliers | 128x128 per core |
| RAM | 128 GB high-speed |

### Architettura

- **VPU**: Vector Processing Unit (tradizionale)
- **MXU**: Matrix Multiply Unit (128x128, specializzato ML)

---

## Salvataggio/Caricamento Modelli

### Salvare Localmente

```python
save_locally = tf.saved_model.SaveOptions(experimental_io_device='/job:localhost')
model.save('./model', options=save_locally)
```

### Caricare da Disco Locale

```python
with tpu_strategy.scope():
    load_locally = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
    model = tf.keras.models.load_model('./model', options=load_locally)
```

### Checkpoint durante Training

```python
save_locally = tf.saved_model.SaveOptions(experimental_io_device='/job:localhost')
checkpoints_cb = tf.keras.callbacks.ModelCheckpoint('./checkpoints', options=save_locally)
model.fit(..., callbacks=[checkpoints_cb])
```

### Caricare da TensorFlow Hub

```python
import tensorflow_hub as hub

with tpu_strategy.scope():
    load_locally = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
    pretrained_model = hub.KerasLayer(
        'https://tfhub.dev/tensorflow/efficientnet/b6/feature-vector/1',
        trainable=True,
        input_shape=[512,512,3],
        load_options=load_locally
    )
```

---

## TPU nelle Code Competitions

Alcune competizioni code-only NON supportano submission TPU. Workaround:

### Step 1: Training su TPU (notebook separato)

```python
# Train su TPU
model.fit(...)

# Salva modello
model.save('model.h5')
```

### Step 2: Crea Dataset dall'Output

Crea un dataset Kaggle dai file output del notebook.

### Step 3: Inference su GPU (notebook submission)

```python
# Carica modello e fai inference con GPU
model = tf.keras.models.load_model('../input/yourDataset/model.h5')
predictions = model.predict(test_data)
```

---

## TPU in PyTorch

### Setup

```bash
# Installa Torch-XLA
!curl https://raw.githubusercontent.com/pytorch/xla/master/contrib/scripts/env-setup.py -o pytorch-xla-env-setup.py
!python pytorch-xla-env-setup.py --version nightly --apt-packages libomp5 libopenblas-dev
```

### Checklist PyTorch + TPU

```python
# 1. Spawn multiprocessing
import torch_xla.core.xla_model as xm
import torch_xla.distributed.parallel_loader as pl
import torch_xla.distributed.xla_multiprocessing as xmp

xmp.spawn(_mp_fn, nprocs=8, start_method='fork')

# 2. Wrappa modello
MX = xmp.MpModelWrapper(JigsawModel())

# 3. Invia a device TPU
device = xm.xla_device()
model = MX.to(device)

# 4. Training loop - invia dati a device
ids = ids.to(device, dtype=torch.long)
targets = targets.to(device, dtype=torch.float)

# 5. Stampe
xm.master_print("message")

# 6. Data loading distribuito
train_sampler = torch.utils.data.distributed.DistributedSampler(
    train_dataset,
    num_replicas=xm.xrt_world_size(),
    rank=xm.get_ordinal()
)

# 7. Training con ParallelLoader
para_loader = pl.ParallelLoader(train_data_loader, [device])
train_fn(para_loader.per_device_loader(device))

# 8. Aggrega risultati
xm.mesh_reduce('result', result, reduce_fn)

# 9. Salva modello (ottimizzato)
import torch_xla.utils.serialization as xser
xser.save(model.state_dict(), "model.bin", master_only=True)
```

---

## Risorse

### Tutorial Ufficiali

- [Five flowers with Keras and Xception on TPU](https://www.kaggle.com/code/mgorner/five-flowers-with-keras-and-xception-on-tpu)
- [Keras and modern convnets on TPUs](https://codelabs.developers.google.com/codelabs/keras-flowers-tpu/)
- [Getting Started With TPUs (Video)](https://youtu.be/1pdwRQ1DQfY)

### Playground Competition

- [Flower Classification with TPUs](https://www.kaggle.com/c/flower-classification-with-tpus)
- [Create Your First Submission](https://www.kaggle.com/kernels/fork/10204702)

### Documentazione

- [Official TPU Documentation](https://docs.cloud.google.com/tpu/docs)

---

## Quick Reference per Agenti AI

### Quando Usare TPU vs GPU

| Scenario | TPU | GPU |
|----------|:---:|:---:|
| Large batch training | ✅ | ⚠️ |
| Image models (ResNet, EfficientNet) | ✅ | ✅ |
| Transformer models | ✅ | ✅ |
| Custom training loops | ⚠️ | ✅ |
| Small datasets | ❌ | ✅ |
| Debugging | ❌ | ✅ |

### Checklist Pre-Training TPU

1. ✅ Dati su GCS in formato TFRecord
2. ✅ Batch size >= 64 per core (512+ totale)
3. ✅ Learning rate scalato proporzionalmente
4. ✅ `steps_per_execution` configurato
5. ✅ Strategia TPU inizializzata
6. ✅ Modello creato nello scope

---

*Documento per Team AI - Sfrutta la potenza dei TPU!*
