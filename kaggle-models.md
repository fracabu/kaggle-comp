# Kaggle Models - Modelli Pre-Trainati

> Repository di modelli ML pre-trainati pronti all'uso, inclusi LLM e modelli di diffusione.

---

## Modelli Trending

### Top Community Models

| Modello | Autore | Tipo | Notebooks | Descrizione |
|---------|--------|------|-----------|-------------|
| **Gemma** | Google | LLM | 383 | Famiglia di modelli lightweight e open, basati sulla tecnologia Gemini |
| **Cats vs Dogs Classifier** | Wafaa EL HUSSEINI | MobileNet V2 | 1 | Fine-tuned per classificazione immagini (~99% accuracy) |
| **Vesuvius Surface Detection** | Innat | - | 0 | Per la competizione Vesuvius Challenge |

---

## Modelli Hugging Face Integrati

| Modello | Notebooks | Uso |
|---------|-----------|-----|
| **sentence-transformers/all-MiniLM-L6-v2** | 1,067 | Sentence embeddings |
| **google-bert/bert-base-uncased** | 939 | NLP tasks |
| **openai-community/gpt2** | 342 | Text generation |
| **distilbert/distilbert-base-uncased** | 341 | NLP leggero |

---

## Modelli per Task

### Audio Event Classification

| Modello | Publisher | Descrizione |
|---------|-----------|-------------|
| **Perch (Bird Vocalization Classifier)** | Google | Classificatore globale per vocalizzazioni di uccelli |
| **YAMNet** | Google | Classificatore audio trainato su AudioSet |
| **Trillsson** | Google | Speech embeddings paralinguistici |

### Object Detection

| Modello | Publisher | Descrizione |
|---------|-----------|-------------|
| **YOLOV8** | Keras | Architettura YOLO per object detection |
| **Ultralytics YOLO11** | Ultralytics | Detection, tracking, segmentation, pose estimation |
| **MobileNet V2** | Google | Object detection basato su SSD, trainato su Open Images V4 |

### Pose Detection

| Modello | Publisher | Descrizione |
|---------|-----------|-------------|
| **MoveNet** | Google | Predizione joint locations su immagini RGB |
| **Handpose 3D** | MediaPipe | Rilevamento pose delle mani |

### Image Classification

| Modello | Publisher | Descrizione |
|---------|-----------|-------------|
| **Traffic Sign Detection** | Sachin-NK | Rilevamento segnali stradali |
| **ViT FineTuned CIFAR** | otvxcodes | Vision Transformer fine-tuned |

---

## Guide per l'Uso dei Modelli

### Per tipo di dati:

| Guida | Link |
|-------|------|
| **Modelli per Immagini** | [learn-guide/models-image-data](https://www.kaggle.com/learn-guide/models-image-data) |
| **Modelli per Testo** | [learn-guide/models-text-data](https://www.kaggle.com/learn-guide/models-text-data) |
| **Modelli per Audio** | [learn-guide/models-audio-data](https://www.kaggle.com/learn-guide/models-audio-data) |

---

## Come Usare i Modelli

### Con kagglehub

```python
import kagglehub

# Scarica un modello
path = kagglehub.model_download("google/gemma/keras/gemma_2b_en")

# Usa il modello
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(path)
```

### In un Notebook Kaggle

1. Vai alla pagina del modello
2. Clicca "Add to Notebook"
3. Il modello sarà disponibile in `/kaggle/input/`

---

## Modelli Consigliati per fcWebDev

### Per iniziare (Computer Vision)
- **MobileNet V2** - Leggero e versatile
- **YOLOV8** - Object detection SOTA

### Per NLP
- **all-MiniLM-L6-v2** - Sentence embeddings veloci
- **distilbert-base-uncased** - BERT leggero

### Per competizioni
- **Gemma** - LLM di Google, ottimo per task di testo
- **Perch** - Se vuoi fare audio classification

---

## Publisher Principali

- **Google** - Gemma, MobileNet, MoveNet, YAMNet
- **Keras** - YOLOV8, architetture standard
- **Ultralytics** - YOLO11
- **MediaPipe** - Handpose, pose detection
- **Hugging Face** - Integrazione con migliaia di modelli

---

*Documento generato l'11 Dicembre 2024*
