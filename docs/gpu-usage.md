# Efficient GPU Usage - Tips e Best Practices

> Come ottenere il massimo dalle GPU gratuite NVIDIA Tesla P100 su Kaggle.

---

## Overview

Kaggle fornisce **accesso gratuito** a GPU NVIDIA TESLA P100.

### Quota Settimanale

- **30 ore/settimana** (o più in base alla domanda)
- La quota si resetta settimanalmente
- Utile per training deep learning (TensorFlow, PyTorch)
- NON accelera pandas, scikit-learn, etc.

---

## Tips per Massimizzare l'Uso

### 1. Attiva GPU Solo Quando Necessario

Le GPU sono utili SOLO se usi librerie che le sfruttano:
- TensorFlow
- PyTorch
- Keras
- Altri framework GPU-accelerated

**NON usare GPU per:**
- Data manipulation con pandas
- Preprocessing con scikit-learn
- Analisi esplorativa (EDA)

### 2. Monitora il Tuo Utilizzo

Kaggle offre strumenti per monitorare l'uso GPU:
- Settings menu nel Notebook editor
- Top della pagina kaggle.com/notebooks
- Pagina del tuo profilo
- Finestra session management

### 3. Evita Batch Sessions per Salvare

**NON usare "Commit"** solo per salvare progressi!

I batch sessions (commit) eseguono TUTTO il codice da capo. Invece:
- Scarica il file `.ipynb` dal Notebook editor
- Più efficiente e non spreca quota

### 4. Cancella Batch Sessions Non Necessari

Se premi "Commit" prima che il primo finisca:
- Avrai multiple sessioni concorrenti
- Cancella la prima se hai aggiornato il codice
- Tieni solo la sessione più recente

### 5. Ferma le Sessioni Interattive

Le sessioni interattive restano attive fino al **timeout di 60 minuti**.

**Prima di chiudere la finestra:**
1. Ferma la sessione manualmente
2. Usa la finestra "Active Events" (angolo in basso a sinistra)
3. Risparmia fino a 60 minuti di compute!

[Scopri di più su Active Events](https://www.kaggle.com/product-feedback/193925)

### 6. Usa la Kaggle API

Per evitare sessioni interattive:

```bash
# Push nuova versione senza aprire l'editor
kaggle kernels push -p /path/to/folder
```

Questo esegue il notebook senza sessione interattiva!

---

## Quando Usare GPU vs CPU

| Task | GPU | CPU |
|------|:---:|:---:|
| Training Neural Networks | ✅ | ❌ |
| Image Classification | ✅ | ❌ |
| NLP con Transformers | ✅ | ❌ |
| Data Loading/Preprocessing | ❌ | ✅ |
| EDA/Visualizzazioni | ❌ | ✅ |
| scikit-learn models | ❌ | ✅ |
| XGBoost/LightGBM | ⚠️ | ✅ |

⚠️ = Dipende dalla configurazione

---

## Specifiche GPU

| Specifica | Valore |
|-----------|--------|
| Modello | NVIDIA Tesla P100 |
| VRAM | 16 GB |
| CUDA Cores | 3584 |
| Prestazioni | ~9.3 TFLOPS FP32 |

---

## Workflow Ottimale per Competizioni

### Fase 1: EDA e Feature Engineering (NO GPU)
```python
# Disabilita GPU per questa fase
# Solo CPU per pandas, matplotlib, seaborn
```

### Fase 2: Training Modello (CON GPU)
```python
# Attiva GPU per training
# Salva checkpoint frequentemente
# Monitora il tempo rimanente
```

### Fase 3: Inference (Dipende)
```python
# GPU se batch grande
# CPU se inference piccola
```

---

## Errori Comuni da Evitare

1. **Lasciare GPU attiva durante preprocessing**
2. **Dimenticare sessioni aperte**
3. **Commit multipli non necessari**
4. **Non salvare checkpoint del modello**
5. **Training troppo lungo senza monitoring**

---

## Code Snippets Utili

### Check GPU Disponibile

```python
import tensorflow as tf
print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))

# PyTorch
import torch
print("CUDA available:", torch.cuda.is_available())
print("GPU name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A")
```

### Monitorare Memoria GPU

```python
# PyTorch
import torch
print(f"Allocated: {torch.cuda.memory_allocated()/1e9:.2f} GB")
print(f"Cached: {torch.cuda.memory_reserved()/1e9:.2f} GB")

# Clear cache
torch.cuda.empty_cache()
```

### Mixed Precision Training (Risparmia VRAM)

```python
# PyTorch
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()

with autocast():
    output = model(input)
    loss = criterion(output, target)

scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()
```

---

## Link Utili

- [Tutorial GPU di Dan Becker](https://www.kaggle.com/dansbecker/running-kaggle-kernels-with-a-gpu)
- [Kaggle Docker Python](https://github.com/Kaggle/docker-python)
- [Kaggle Docker R](https://github.com/Kaggle/docker-rstats)

---

*Documento per Team AI - Ottimizza le tue risorse GPU!*
