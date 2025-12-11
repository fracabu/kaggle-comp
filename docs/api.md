# Kaggle Public API - Documentazione Completa

> API per interagire programmaticamente con Kaggle: competizioni, dataset, notebook e modelli.

---

## Installazione e Autenticazione

### Installazione

```bash
pip install kaggle
```

Su Mac/Linux potrebbe essere necessario:
```bash
pip install --user kaggle
```

Se ricevi l'errore `kaggle: command not found`, assicurati che i binari Python siano nel PATH:
- **Linux**: `~/.local/bin`
- **Windows**: `$PYTHON_HOME/Scripts`

### Autenticazione

1. Vai su [Account Settings](https://www.kaggle.com/settings/account)
2. Clicca "Create New Token"
3. Scarica `kaggle.json`
4. Posiziona il file:
   - **Linux/Mac**: `~/.kaggle/kaggle.json`
   - **Windows**: `C:\Users\<username>\.kaggle\kaggle.json`

---

## Interazione con Competizioni

### Comandi Principali

```bash
# Lista competizioni attive
kaggle competitions list

# Scarica dati di una competizione
kaggle competitions download -c [COMPETITION]

# Invia submission
kaggle competitions submit -c [COMPETITION] -f [FILE] -m [MESSAGE]

# Lista submission precedenti
kaggle competitions submissions -c [COMPETITION]
```

### Note Importanti

- Devi accettare le regole della competizione sul sito prima di scaricare i dati
- Non puoi accettare le regole via API
- Usa `-h` dopo qualsiasi comando per vedere l'help

---

## Interazione con Dataset

### Comandi Principali

```bash
# Cerca dataset
kaggle datasets list -s [KEYWORD]

# Scarica dataset
kaggle datasets download -d [DATASET]
```

### Creare un Nuovo Dataset

```bash
# 1. Crea cartella con i file
mkdir my-dataset

# 2. Genera metadata
kaggle datasets init -p /path/to/dataset

# 3. Modifica datapackage.json con i metadati

# 4. Crea il dataset
kaggle datasets create -p /path/to/dataset
```

### Aggiornare un Dataset Esistente

```bash
# 1. Genera/aggiorna metadata
kaggle datasets init -p /path/to/dataset

# 2. Verifica che l'id in dataset-metadata.json sia corretto

# 3. Crea nuova versione
kaggle datasets version -p /path/to/dataset -m "Your message here"
```

### Tool Utili

- **[Frictionless Data Package Creator](http://create.frictionlessdata.io/)** - Per completare velocemente il file metadata
- **[DataStudio Kaggle Connector](https://datastudio.google.com/datasources/create?connectorId=AKfycbz8WVuZI1FRHJM3g_ucqP-L7B9EIIPDsC9RofvZk1Xw-bD6p55SNjs7JudEsOYK1o2t)** - Importa dataset direttamente in DataStudio

---

## Interazione con Notebook

### Comandi Principali

```bash
# Cerca notebook
kaggle kernels list -s [KEYWORD]

# Push notebook su Kaggle
kaggle kernels push -k [KERNEL] -p /path/to/folder

# Scarica notebook e metadata
kaggle kernels pull [KERNEL] -p /path/to/download -m
```

### Creare e Eseguire un Notebook

```bash
# 1. Crea cartella con i file di codice
mkdir my-notebook

# 2. Genera metadata
kaggle kernels init -p /path/to/folder

# 3. Modifica kernel-metadata.json

# 4. Push e run
kaggle kernels push -p /path/to/folder
```

### Creare Nuova Versione

```bash
# 1. Scarica versione corrente
kaggle kernels pull [KERNEL] -p /path/to/download -m

# 2. Verifica id in kernel-metadata.json

# 3. Push nuova versione
kaggle kernels push -p /path/to/folder
```

---

## Interazione con Modelli

### Usando kagglehub (Raccomandato)

```python
import kagglehub

# Autenticazione
kagglehub.login()

# Scarica ultima versione
path = kagglehub.model_download("google/gemma/pyTorch/2b")

# Scarica versione specifica
path = kagglehub.model_download("google/gemma/pyTorch/2b/1")

print("Path to model files:", path)
```

### Upload Modelli

```python
import kagglehub
from kagglehub.config import get_kaggle_credentials

kagglehub.login()
username, _ = get_kaggle_credentials()

# Upload modello (PyTorch, JAX, o other)
kagglehub.model_upload(
    f'{username}/my_model/pyTorch/2b',
    'path/to/local/model/files',
    'Apache 2.0'
)
```

### Usando CLI

```bash
# Scarica modello
kaggle models instances versions download google/gemma/pyTorch/2b/1
```

### Usando API Direttamente

```bash
# Imposta credenziali
export KAGGLE_USERNAME=xyz
export KAGGLE_KEY=xyz

# Con curl
curl -L -o model.tar.gz \
  https://www.kaggle.com/api/v1/models/google/gemma/pyTorch/2b/1/download \
  -u $KAGGLE_USERNAME:$KAGGLE_KEY

# Con wget
wget https://www.kaggle.com/api/v1/models/google/gemma/pyTorch/2b/1/download \
  --user=$KAGGLE_USERNAME --password=$KAGGLE_KEY --auth-no-challenge
```

---

## Rate Limits

Kaggle utilizza rate limiting dinamico sia sull'API pubblica che sul sito.

**Se ricevi errore 429 "Too many requests":**
- Aspetta e riprova più tardi
- Se pensi sia un bug, segnalalo nel forum [Product Feedback](https://www.kaggle.com/discussions/product-feedback)

---

## Risorse Utili

- [Documentazione GitHub Kaggle API](https://github.com/Kaggle/kaggle-api)
- [Changelog](https://github.com/Kaggle/kaggle-api/blob/master/CHANGELOG.md)
- [Kagglehub Documentation](https://github.com/Kaggle/kagglehub)
- [Dataset Metadata Wiki](https://github.com/Kaggle/kaggle-api/wiki/Dataset-Metadata)
- [Kernel Metadata Wiki](https://github.com/Kaggle/kaggle-api/wiki/Kernel-Metadata)

---

## Quick Reference per Agenti AI

### Workflow Tipico Competizione

```bash
# 1. Lista competizioni
kaggle competitions list

# 2. Scarica dati
kaggle competitions download -c titanic

# 3. Analizza e crea modello (localmente)

# 4. Invia submission
kaggle competitions submit -c titanic -f submission.csv -m "First attempt"

# 5. Controlla risultati
kaggle competitions submissions -c titanic
```

### Workflow Tipico Dataset

```bash
# 1. Cerca
kaggle datasets list -s "cybersecurity"

# 2. Scarica
kaggle datasets download -d fcwebdev/synthetic-cybersecurity-logs

# 3. Analizza localmente
```

---

*Documento generato per il Team AI Data Scientists - Dicembre 2024*
