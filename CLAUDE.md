# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **knowledge base for AI agents** participating in Kaggle competitions. It contains documentation, guides, and resources for the Kaggle account `fcwebdev` (Francesco Capurso).

## Repository Structure

- `GUIDA-TEAM-AI-KAGGLE.md` - Main guide with team mission, workflow, and quick reference
- `profilo-kaggle.md` - Profile information and stats
- `competizioni-attive.md` - Active competitions with prizes and deadlines
- `kaggle-learn-corsi.md` - Free Kaggle courses
- `kaggle-models.md` - Pre-trained models reference
- `docs/` - Detailed technical documentation:
  - `api.md` - Kaggle API commands and authentication
  - `gpu-usage.md` - GPU optimization tips (Tesla P100)
  - `tpu.md` - TPU guide (v3-8)
  - `notebooks.md` - Kaggle notebook environment

## Kaggle API Commands

```bash
# Setup credentials: ~/.kaggle/kaggle.json
pip install kaggle kagglehub

# Competitions
kaggle competitions list
kaggle competitions download -c [COMPETITION]
kaggle competitions submit -c [COMPETITION] -f submission.csv -m "message"
kaggle competitions submissions -c [COMPETITION]

# Datasets
kaggle datasets list -s [KEYWORD]
kaggle datasets download -d [DATASET]

# Notebooks (push without interactive session)
kaggle kernels push -p /path/to/folder

# Models
import kagglehub
path = kagglehub.model_download("google/gemma/pyTorch/2b")
```

## Competition Workflow

1. **EDA (CPU only)** - Data exploration with pandas, matplotlib, seaborn
2. **Feature Engineering (CPU)** - Preprocessing, encoding, scaling
3. **Baseline Model (CPU)** - Quick model with sklearn for initial submission
4. **Model Training (GPU/TPU)** - Deep learning with TensorFlow/PyTorch
5. **Ensemble & Submission** - Combine models, generate submission.csv

## Compute Resources

| Resource | Quota | Best For |
|----------|-------|----------|
| GPU (Tesla P100) | 30 hrs/week | Deep learning, CNN, Transformers |
| TPU (v3-8) | 20 hrs/week | Large batch training, TensorFlow |

**GPU tips**: Don't use for pandas/sklearn. Stop sessions before closing. Use API to avoid interactive sessions.

## Data Paths in Kaggle Notebooks

```python
# Input data
train = pd.read_csv('/kaggle/input/[competition]/train.csv')

# Output (20 GB max)
submission.to_csv('/kaggle/working/submission.csv', index=False)
```

## Key Metrics to Monitor

- Cross-validation score vs leaderboard score (detect overfitting)
- Submission count (limited per competition)
- Time remaining
- GPU/TPU quota usage
