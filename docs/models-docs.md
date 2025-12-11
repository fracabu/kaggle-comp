# Kaggle Models - Documentazione Tecnica

> Repository di modelli pre-trainati integrato con competizioni e notebook Kaggle.

---

## Cos'è Kaggle Models

Kaggle Models è un repository di modelli pre-trainati per ML e Generative AI, profondamente integrato con la piattaforma Kaggle.

### Fonti dei Modelli

- **Partner**: Meta (Llama 2), Alibaba (Qwen), Google (Gemma)
- **Integrazioni**: Keras, Hugging Face Hub
- **Community**: Fine-tuned variants e innovazioni

---

## Trovare Modelli

### Filtri Disponibili

| Filtro | Opzioni |
|--------|---------|
| Sorgente | Organization, Community, Hugging Face |
| Framework | PyTorch, TensorFlow, JAX, etc. |
| Task | Classification, Generation, etc. |
| Size | Numero di parametri |
| Sort | Upvotes, Downloads, etc. |

### Dove Cercare

1. **[Models Landing Page](https://www.kaggle.com/models)** - Ricerca principale
2. **Tab "Models" nelle competizioni** - Modelli popolari per task specifici
3. **"Add Models" nel notebook editor** - Ricerca e aggiungi direttamente

### Struttura Detail Page

- **Overview**: Model Card con metadata
- **Variations**: Stesso modello con parametri diversi (small, medium, large)
- **Frameworks**: Compatibilità (TensorFlow, PyTorch, etc.)
- **Usage Dashboard**: Statistiche di utilizzo

---

## Usare Modelli

### Su Kaggle (Notebooks)

#### Metodo 1: Fork Notebook Esistente
I modelli attached vengono copiati automaticamente.

#### Metodo 2: Nuovo Notebook da Model Page
1. Vai alla pagina del modello
2. Click "New Notebook"
3. Seleziona framework e variation
4. Copia starter code

#### Metodo 3: Aggiungi a Notebook Esistente
1. Apri notebook editor
2. Panel destro → "Add Models"
3. Cerca e aggiungi

#### Hugging Face Models
Se usi la libreria Transformers, il modello viene attached automaticamente.

### Fuori da Kaggle

#### Metodo 1: kagglehub (Raccomandato)

```python
import kagglehub

# Autenticazione (per modelli gated come Gemma)
kagglehub.login()

# Scarica ultima versione
path = kagglehub.model_download("google/gemma/pyTorch/2b")

# Scarica versione specifica
path = kagglehub.model_download("google/gemma/pyTorch/2b/1")

print("Path to model files:", path)
```

#### Metodo 2: Kaggle CLI

```bash
# Configura credenziali prima
kaggle models instances versions download google/gemma/pyTorch/2b/1
```

#### Metodo 3: API Diretta

```bash
export KAGGLE_USERNAME=xyz
export KAGGLE_KEY=xyz

# Con curl
curl -L -o model.tar.gz \
  https://www.kaggle.com/api/v1/models/google/gemma/pyTorch/2b/1/download \
  -u $KAGGLE_USERNAME:$KAGGLE_KEY
```

---

## Creare un Modello

### Upload con kagglehub (Preferito)

```python
import kagglehub
from kagglehub.config import get_kaggle_credentials

kagglehub.login()
username, _ = get_kaggle_credentials()

# Upload (framework: pyTorch, jax, other)
kagglehub.model_upload(
    f'{username}/my_model/pyTorch/2b',
    'path/to/local/model/files',
    'Apache 2.0'
)

# Nuova versione = stesso comando
```

### Upload con CLI

```bash
MODEL_DIR="path/to/local/my-model"
MODEL_VARIATION_DIR="path/to/local/my-model-variation"

# Crea modello
kaggle models init -p $MODEL_DIR
# Modifica model-metadata.json
kaggle models create -p $MODEL_DIR

# Crea variation
kaggle models instances init -p $MODEL_VARIATION_DIR
# Modifica model-instance-metadata.json
kaggle models instances create -p $MODEL_VARIATION_DIR

# Nuova versione
kaggle models instances versions create -p $MODEL_VARIATION_DIR \
  --version-notes "Made it better" \
  $USERNAME/$MODEL_SLUG/$FRAMEWORK/$VARIATION_SLUG
```

### Upload via UI

1. Vai a [kaggle.com/models?new=true](https://www.kaggle.com/models?new=true)
2. Compila form e seleziona "Creating As"
3. Per nuove variations: "Model Variations" → "New Variation"

### Via Hugging Face Integration

1. Vai al tuo modello su Hugging Face
2. Click "Use this model"
3. Seleziona "Kaggle" dal dropdown
4. Crea notebook e salva versione

---

## Naming Convention

### Handle Format

```
owner_slug/model_slug/framework/variation_slug/version_number
```

| Componente | Descrizione | Esempio |
|------------|-------------|---------|
| owner_slug | Username o org | google |
| model_slug | Nome famiglia modello | gemma |
| framework | Framework ML | pyTorch |
| variation_slug | Dettagli specifici | 2b-it |
| version_number | Numero versione | 1 |

### Cosa Includere nella Variation

- **Model Size**: 7b, 13b, 70b
- **Optimization**: int4, int8, distilled
- **Task**: chat, instruct, code
- **Training**: instruction-tuned, prompt-tuned
- **Language**: en, it, multilingual
- **Hardware**: gpu, cpu, tpu

### Esempi Reali

| Handle | Note |
|--------|------|
| `google/gemma-2/gguf/2.0-27b-it/1` | 27B params, instruction tuned |
| `google/gemma/tfLite/gemma-2b-it-gpu-int4/1` | 2B, instruct, GPU, int4 quantization |
| `metaresearch/llama-3/pyTorch/70b-chat` | 70B, chat variant |
| `deepmind/biggan/tensorFlow1/128` | 128x128 image generation |

---

## Modelli Gated

Alcuni modelli richiedono accettazione di licenze specifiche.

### Per Utenti

1. Vai alla pagina del modello
2. Accetta agreement
3. Attendi approvazione (automatic o manual)
4. Status: pending → accepted → accesso

### Per Publisher (Organizations)

#### Setup Gating

1. Contatta Kaggle per permessi
2. Abilita gating in "Settings"
3. Configura agreement in YAML:
   - Title, description
   - Privacy policy URL
   - Form fields per raccolta dati
   - Review mode (automatic/manual)

#### Gating Publisher API

Base URL: `https://www.kaggle.com`
Auth: HTTP Basic con username:key

```bash
# Lista consents
GET /api/v1/models/{owner}/{model}/user-consents
    ?review_status=pending
    &is_user_request_data_expired=false
    &next_page_token=...

# Review consent
POST /api/v1/models/{owner}/{model}/user-consents/review
    Body: {
        "user_name": "username",
        "review_status": "accepted",  # pending, accepted, rejected
        "publisher_notes": "optional notes"
    }
```

---

## Import Model Versions

Copia versioni da un modello a un altro:

1. Vai al modello target
2. Click "︙" → "Import Versions"
3. Seleziona modello sorgente
4. Seleziona versioni da importare
5. Conferma e importa

**Note:**
- Solo modelli che possiedi o sei collaboratore
- Private → Public è irreversibile
- Mantiene framework e variation slug originali

---

## Best Practices per Team AI

### Selezione Modello per Competizione

1. **Controlla Tab "Models"** nella competizione
2. **Leggi notebook vincenti** precedenti
3. **Valuta trade-off** size vs performance
4. **Considera** tempo di inference per submission

### Workflow Raccomandato

```python
# 1. Scarica modello
import kagglehub
path = kagglehub.model_download("google/gemma/pyTorch/2b")

# 2. Fine-tune sul task
# ... training code ...

# 3. Salva versione fine-tuned
kagglehub.model_upload(
    f'{username}/gemma-competition-finetuned/pyTorch/2b',
    './finetuned_model',
    'Apache 2.0'
)

# 4. Usa nel notebook di submission
```

---

*Documento per Team AI - Repository modelli per vincere competizioni!*
