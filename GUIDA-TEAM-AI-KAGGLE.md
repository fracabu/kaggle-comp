# GUIDA DEFINITIVA - Team AI Data Scientists per Kaggle

> Knowledge Base per Agenti AI che partecipano a competizioni Kaggle

---

## Indice

1. [Obiettivo del Team](#obiettivo-del-team)
2. [Profilo Kaggle](#profilo-kaggle)
3. [Struttura Documentazione](#struttura-documentazione)
4. [Quick Start Competizioni](#quick-start-competizioni)
5. [Risorse Compute](#risorse-compute)
6. [Workflow Vincente](#workflow-vincente)
7. [API e Automazione](#api-e-automazione)
8. [Modelli Pre-Trainati](#modelli-pre-trainati)
9. [Collaborazione Team](#collaborazione-team)
10. [Checklist Pre-Competition](#checklist-pre-competition)

---

## Obiettivo del Team

**Mission**: Creare un team di agenti AI che:
- Partecipa a competizioni Kaggle
- Raggiunge posizioni top nelle leaderboard
- Costruisce visibilità nel panorama data science
- Attrae opportunità professionali

---

## Profilo Kaggle

### Account: fcWebDev

| Info | Valore |
|------|--------|
| **Username** | fcwebdev |
| **Location** | Rome, Italy |
| **Occupation** | Junior Data Analyst |
| **Competizioni** | 1 |
| **Datasets** | 3 |
| **Notebooks** | 1 |

### Following Strategici
- **Chris Deotte** - Kaggle Grandmaster (notebooks eccellenti)
- **Alexis Cook** - Kaggle Staff

### Dataset Pubblicato
- Synthetic Cybersecurity Logs for Anomaly Detection

---

## Struttura Documentazione

```
kaggle-comp/
├── GUIDA-TEAM-AI-KAGGLE.md      # Questa guida
├── profilo-kaggle.md             # Profilo utente
├── competizioni-attive.md        # Lista competizioni con premi
├── kaggle-learn-corsi.md         # Corsi gratuiti
├── kaggle-models.md              # Modelli trending
├── kaggle-benchmarks.md          # Benchmark AI
├── kaggle-host-competition.md    # Come hostare
└── docs/
    ├── api.md                    # API Reference
    ├── gpu-usage.md              # Tips GPU
    ├── tpu.md                    # Guida TPU
    ├── models-docs.md            # Documentazione modelli
    ├── organizations.md          # Organizzazioni
    ├── groups.md                 # Gruppi/Collaborazione
    ├── notebooks.md              # Ambiente notebook
    ├── blog-news.md              # News Kaggle
    └── edu.md                    # Formazione
```

---

## Quick Start Competizioni

### Competizioni Raccomandate per Iniziare

| Competizione | Tipo | Difficoltà | Note |
|-------------|------|------------|------|
| **Titanic** | Classification | Facile | Hai già un progetto! |
| **House Prices** | Regression | Facile | Feature engineering |
| **Diabetes Prediction** | Playground | Media | Attiva ora |
| **Spaceship Titanic** | Classification | Media | Simile a Titanic |

### Competizioni con Premi Alti

| Competizione | Premio | Scadenza |
|-------------|--------|----------|
| AI Mathematical Olympiad | $2.2M | 4 mesi |
| Hull Tactical | $100k | 5 giorni |
| Vesuvius Challenge | $100k | 2 mesi |
| MITSUI Commodity | $100k | 1 mese |

---

## Risorse Compute

### GPU (Tesla P100)

| Risorsa | Limite |
|---------|--------|
| Quota | 30 ore/settimana |
| VRAM | 16 GB |
| Best for | Deep Learning, CNN, Transformers |

**Tips**:
- NON usare per pandas/sklearn
- Ferma sessioni prima di chiudere
- Usa API per evitare sessioni interattive

### TPU (v3-8)

| Risorsa | Limite |
|---------|--------|
| Quota | 20 ore/settimana |
| Max sessione | 9 ore |
| RAM | 128 GB |
| Best for | Large batch training, TensorFlow |

**Tips**:
- Batch size: 128 * 8 = 1024
- Dati su GCS in TFRecords
- Scala learning rate con batch size

---

## Workflow Vincente

### Fase 1: Analisi (CPU Only)

```python
# EDA - NO GPU
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('/kaggle/input/competition/train.csv')

# Analisi esplorativa
print(train.info())
print(train.describe())
# Visualizzazioni...
```

### Fase 2: Feature Engineering (CPU)

```python
# Feature engineering
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Crea features
# Gestisci missing values
# Encoding categoriche
# Scaling numeriche
```

### Fase 3: Baseline Model (CPU/GPU)

```python
# Modello baseline veloce
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

model = RandomForestClassifier(n_estimators=100)
scores = cross_val_score(model, X_train, y_train, cv=5)
print(f"Baseline CV: {scores.mean():.4f}")
```

### Fase 4: Model Training (GPU/TPU)

```python
# Deep Learning con GPU
import tensorflow as tf

# Verifica GPU
print(tf.config.list_physical_devices('GPU'))

# Training model
model = create_model()
model.fit(X_train, y_train,
          validation_split=0.2,
          epochs=50,
          batch_size=32)
```

### Fase 5: Ensemble & Submission

```python
# Ensemble di modelli
predictions = (pred1 * 0.4 + pred2 * 0.3 + pred3 * 0.3)

# Submission
submission = pd.DataFrame({
    'id': test['id'],
    'target': predictions
})
submission.to_csv('submission.csv', index=False)
```

---

## API e Automazione

### Setup

```bash
pip install kaggle kagglehub
```

### Credenziali

File `~/.kaggle/kaggle.json`:
```json
{"username":"fcwebdev","key":"YOUR_API_KEY"}
```

### Comandi Essenziali

```bash
# Lista competizioni
kaggle competitions list

# Scarica dati
kaggle competitions download -c titanic

# Submit
kaggle competitions submit -c titanic -f submission.csv -m "v1"

# Lista submissions
kaggle competitions submissions -c titanic
```

### Automazione con Python

```python
import subprocess

def submit_prediction(competition, file, message):
    cmd = f"kaggle competitions submit -c {competition} -f {file} -m '{message}'"
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout.decode()
```

---

## Modelli Pre-Trainati

### Download Modelli

```python
import kagglehub

# Modelli popolari
path = kagglehub.model_download("google/gemma/pyTorch/2b")
path = kagglehub.model_download("google/bert/tfLite/uncased-l-12-h-768-a-12")
```

### Modelli Consigliati per Task

| Task | Modello |
|------|---------|
| Text Classification | BERT, DistilBERT |
| Text Generation | Gemma, GPT-2 |
| Image Classification | EfficientNet, ResNet |
| Object Detection | YOLO v8, YOLO v11 |
| Sentence Embeddings | all-MiniLM-L6-v2 |

---

## Collaborazione Team

### Creare Gruppo

1. Avatar → "Your Groups"
2. "New Group" → "AI Competition Team"
3. Invita membri

### Condividere Risorse

1. Vai a notebook/dataset
2. Settings → Collaborators
3. Cerca gruppo
4. Permessi: Can Edit

### Best Practices

- **Notebook per fase**: EDA, Features, Model, Ensemble
- **Versioning**: Salva versioni significative
- **Documentation**: Commenta codice importante
- **Review**: Controlla notebook dei teammate

---

## Checklist Pre-Competition

### Prima di Iniziare

- [ ] Leggere rules e evaluation metric
- [ ] Scaricare e esplorare dati
- [ ] Leggere Discussion forum
- [ ] Studiare notebook pubblici top
- [ ] Identificare approcci vincenti passati

### Durante la Competition

- [ ] Creare baseline submission
- [ ] Iterare su feature engineering
- [ ] Testare diversi modelli
- [ ] Cross-validation robusta
- [ ] Ensemble di modelli
- [ ] Monitorare leaderboard

### Pre-Deadline

- [ ] Selezionare submission finali
- [ ] Verificare no data leakage
- [ ] Test submission format
- [ ] Documentare approccio

---

## Risorse Aggiuntive

### Corsi Consigliati (Kaggle Learn)

1. Python
2. Pandas
3. Intro to Machine Learning
4. Intermediate ML
5. Feature Engineering
6. Intro to Deep Learning

### Documentazione Completa

Vedi cartella `docs/` per guide dettagliate su:
- API Kaggle
- GPU/TPU Usage
- Modelli
- Notebook Environment
- Collaborazione

---

## Contatti e Link

- **Profilo**: [kaggle.com/fcwebdev](https://www.kaggle.com/fcwebdev)
- **GitHub**: [github.com/fracabu](https://github.com/fracabu)
- **Portfolio**: [titanic-ml-kaggle.streamlit.app](https://titanic-ml-kaggle.streamlit.app/)

---

## Note per Agenti AI

### Priorità Azioni

1. **Leggi dati** - Comprendi il problema
2. **EDA veloce** - Identifica pattern
3. **Baseline** - Submit rapidamente
4. **Itera** - Migliora incrementalmente
5. **Ensemble** - Combina modelli

### Metriche da Monitorare

- Cross-validation score
- Leaderboard position
- Submission count (limitato!)
- Tempo rimanente

### Red Flags

- Overfitting (CV >> LB)
- Data leakage
- Target leakage
- Submission format errato

---

*Documento generato per Team AI Data Scientists*
*Versione 1.0 - Dicembre 2024*
