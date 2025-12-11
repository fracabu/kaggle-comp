# Kaggle Knowledge Base

Knowledge base e dashboard per partecipare a competizioni Kaggle. Account: [fcwebdev](https://www.kaggle.com/fcwebdev)

## Panoramica

Questo repository contiene:
- Documentazione su API, GPU/TPU, notebook Kaggle
- Guide per competizioni e workflow
- Dashboard Streamlit per monitorare le competizioni

## Competizioni

| Competizione | Tipo | Risultato |
|-------------|------|-----------|
| Insurance Regression (S4E12) | Playground | 430/2390 |
| Gemini 3 Hackathon | Hackathon | In corso |

## Quick Start

```bash
# Installa dipendenze
pip install -r requirements.txt

# Avvia dashboard
streamlit run app.py
```

## Struttura Repository

```
kaggle-comp/
├── app.py                    # Dashboard Streamlit
├── requirements.txt          # Dipendenze Python
├── GUIDA-TEAM-AI-KAGGLE.md   # Guida principale
├── profilo-kaggle.md         # Info profilo
├── competizioni-attive.md    # Competizioni con premi
├── kaggle-learn-corsi.md     # Corsi gratuiti
├── kaggle-models.md          # Modelli pre-trainati
└── docs/
    ├── api.md                # Kaggle API reference
    ├── gpu-usage.md          # Ottimizzazione GPU (Tesla P100)
    ├── tpu.md                # Guida TPU (v3-8)
    └── notebooks.md          # Ambiente notebook
```

## Risorse Compute

| Risorsa | Quota | Best For |
|---------|-------|----------|
| GPU (Tesla P100) | 30 hrs/week | Deep Learning, CNN, Transformers |
| TPU (v3-8) | 20 hrs/week | Large batch training, TensorFlow |

## Workflow Competizioni

1. **EDA** (CPU) - Esplorazione dati
2. **Feature Engineering** (CPU) - Preprocessing
3. **Baseline** (CPU) - Prima submission veloce
4. **Training** (GPU/TPU) - Modelli avanzati
5. **Ensemble** - Combinazione e submission finale

## Links

- [Kaggle Profile](https://www.kaggle.com/fcwebdev)
- [GitHub](https://github.com/fracabu)
- [LinkedIn](https://www.linkedin.com/in/francesco-~-capurso-5801031a9/)

---

*Dashboard e knowledge base per AI Data Scientists*

---
Last updated: December 2025
