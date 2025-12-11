# Kaggle Notebooks - Guida Completa

> Ambiente computazionale cloud per analisi riproducibili e collaborative.

---

## Tipi di Notebook

### Jupyter Notebooks

Il tipo più comune. Celle di:
- **Markdown**: Testo formattato
- **Code**: Python o R

Crea: `+Create > New Notebook`

### Scripts

File che eseguono codice sequenzialmente.

Crea: `File > Editor Type > Script`

Linguaggi: Python, R

### RMarkdown Scripts

Combinazione di R code e Markdown. Preferito dalla community R.

---

## Cercare Notebook

### Dove Cercare

| Luogo | Descrizione |
|-------|-------------|
| **Site Search** | Barra in alto, filtra per "Notebooks" |
| **Homepage** | Newsfeed con attività recenti |
| **[Notebooks Listing](https://www.kaggle.com/notebooks)** | Catalogo completo |
| **Dataset/Competition Pages** | Tab "Notebooks" con i migliori |
| **Tags** | Cerca per topic/tecnica |

### Metodi di Ordinamento

| Sort | Descrizione |
|------|-------------|
| **Hotness** | Interesse attuale (default) |
| **Most Votes** | Più popolari di sempre |
| **Most Comments** | Più discussi |
| **Recently Created** | Stream nuovi notebook |
| **Recently Run** | Attività recente |
| **Relevance** | Per query di ricerca |

### Ricerca per Tag

```
tag:classification
tag:crime
tag:nlp
```

Oppure visita: `kaggle.com/tags/[TAG_NAME]`

---

## Usare l'Editor

### Layout

1. **Editing Window**: Scrivi codice
2. **Console**: Esegui comandi interattivi
3. **Settings Pane**: Configurazioni

### Settings Pane Tabs

| Tab | Funzione |
|-----|----------|
| **Input** | Aggiungi/rimuovi data sources |
| **Output** | Visualizza file generati |
| **Table of Contents** | Naviga headings |
| **Session Options** | Lingua, internet, accelerator, docker |
| **Scheduling** | Esecuzione automatica |

### Versioning

"Save & Run All" crea una **versione**:
- Snapshot completo del lavoro
- Codice compilato
- Log files
- Output files
- Data sources
- Docker image

---

## Aggiungere Data Sources

### Tipi di Input

| Tipo | Come Aggiungere |
|------|-----------------|
| **Models** | Input pane → "Add Input" → cerca |
| **Datasets** | Input pane → "Add Input" → cerca |
| **Competitions** | Input pane → "Add Input" → accetta rules |
| **Other Notebooks** | Output di altri notebook come input |

### Path dei Dati

```python
# Datasets e Competition data
/kaggle/input/[dataset-name]/

# Output del tuo notebook
/kaggle/working/
```

### Limite Output

**20 GB max** salvabili in `/kaggle/working/`

---

## Collaborazione

### Invitare Collaboratori

1. Menu "Share" o "Sharing"
2. Cerca utente
3. Scegli permessi:
   - **Can view** (solo notebook privati)
   - **Can edit**

### Collaborare su Dataset

I collaboratori notebook ≠ collaboratori dataset.

Devi invitare separatamente per ogni risorsa.

---

## Ambiente Notebook

### Docker Container

Ogni notebook gira in un container Docker con:
- Python o R pre-installato
- Pacchetti ML principali
- Ambiente configurato

### Immagini Docker

- **Python**: [github.com/Kaggle/docker-python](https://github.com/Kaggle/docker-python)
- **R**: [github.com/Kaggle/docker-rstats](https://github.com/Kaggle/docker-rstats)

Aggiornate ~ogni 2 settimane.

### Pinning Environment

Settings → Session Options → Environment:
- **Original**: Mantieni versione creazione (riproducibilità)
- **Latest**: Usa pacchetti più recenti

### Modificare Ambiente

#### Pacchetti Temporanei (con Internet)

```python
# Python
!pip install my-new-package
!pip install my-existing-package==X.Y.Z

# R
library(devtools)
install_github("some_user/some_package")
```

#### Dependency Manager (per Competition senza Internet)

1. Settings → Dependency Manager
2. Inserisci comandi pip
3. Genera "Dependency Installation Notebook"
4. Attached automaticamente

---

## Acceleratori

### GPU (Tesla P100)

**Quota**: ~30 ore/settimana

Attiva: Settings → Accelerator → GPU

```python
# Verifica GPU
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

### TPU (v3-8)

**Quota**: 20 ore/settimana, max 9h/sessione

Attiva: Settings → Accelerator → TPU v3-8

Vedi [docs/tpu.md](tpu.md) per dettagli.

---

## Google Cloud Services

⚠️ **Alcuni servizi hanno costi!** Verifica pricing prima di usare.

### Abilitare

1. Menu "Add-ons" → "Google Cloud Services"
2. Collega account GCP
3. Seleziona integrazioni

### BigQuery

```python
PROJECT_ID = 'your-google-cloud-project'
from google.cloud import bigquery
bigquery_client = bigquery.Client(project=PROJECT_ID)
```

Risorse:
- [BigQuery Tutorial](https://www.kaggle.com/jessicali9530/tutorial-how-to-use-bigquery-in-kaggle-kernels)
- [BQML Tutorial](https://www.kaggle.com/rtatman/bigquery-machine-learning-tutorial)

### Google Cloud Storage

```python
PROJECT_ID = 'your-google-cloud-project'
from google.cloud import storage
storage_client = storage.Client(project=PROJECT_ID)
```

---

## Scheduling Notebooks

Esegui notebook automaticamente su schedule.

Settings → Scheduling Options → Configura

---

## Specifiche Tecniche

| Risorsa | Limite |
|---------|--------|
| RAM | 16 GB (CPU), 13 GB (GPU) |
| Disco | 20 GB output |
| Timeout | 9 ore sessione |
| GPU | Tesla P100, 16 GB VRAM |
| TPU | v3-8, 128 GB RAM |

---

## Jupyter Server (Experimental)

Connetti IDE locale a Kaggle compute.

```bash
# Installa
pip install kaggle-jupyter-server

# Connetti
kaggle-jupyter-server start
```

---

## Colab Pro Integration (Experimental)

Aumenta GPU compute collegando Colab Pro.

Settings → "Increase GPU compute with Colab Pro"

---

## Best Practices per Team AI

### Struttura Notebook Competition

```python
# 1. Setup e Import
import pandas as pd
import numpy as np
# ...

# 2. Load Data
train = pd.read_csv('/kaggle/input/competition/train.csv')
test = pd.read_csv('/kaggle/input/competition/test.csv')

# 3. EDA (exploratory data analysis)
# ...

# 4. Feature Engineering
# ...

# 5. Model Training
# ...

# 6. Inference
predictions = model.predict(test)

# 7. Submission
submission = pd.DataFrame({'id': test['id'], 'target': predictions})
submission.to_csv('/kaggle/working/submission.csv', index=False)
```

### Tips Performance

1. **Usa GPU solo per training** - Non per EDA
2. **Checkpoint frequenti** - Salva modelli intermedi
3. **Monitora memoria** - Elimina variabili non necessarie
4. **Batch processing** - Per dataset grandi
5. **Cache preprocessing** - Salva come output, riusa come input

### Workflow Collaborativo

1. **Fork** notebook esistente come base
2. **Modifica** e testa
3. **Condividi** con team via Groups
4. **Itera** insieme
5. **Submit** versione migliore

---

## Link Utili

- [Notebooks Listing](https://www.kaggle.com/notebooks)
- [Docker Python](https://github.com/Kaggle/docker-python)
- [Docker R](https://github.com/Kaggle/docker-rstats)
- [GPU Tutorial](https://www.kaggle.com/dansbecker/running-kaggle-kernels-with-a-gpu)
- [TPU Guide](https://www.kaggle.com/docs/tpu)

---

*Documento per Team AI - Ambiente di sviluppo per competizioni!*
