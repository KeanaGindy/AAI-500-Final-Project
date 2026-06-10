# Predicting 30-Day Heart Failure Readmission

**AAI-500 — Probability and Statistics for Artificial Intelligence**
University of San Diego — Group 4 Final Project

## Team

| Member | Role |
|---|---|
| Ian Schmitt | Team lead |
| Keana Gindlesperger | Member |
| Guna Pasupathy | Member |

## Overview

We look at what is associated with patients being readmitted within 30 days of a
heart failure admission, and compare a few models for predicting it. The dataset
has clinical measurements, treatment flags and a couple of social determinants.

Goals:

1. Clean and check the data.
2. Do EDA and statistical testing.
3. Compare interpretable models and ML classifiers against a baseline.
4. Write up the findings and limitations.

## Dataset

Kaggle *Heart Failure Readmission and Social Determinants of Health* dataset:
3,000 patients × 16 columns. The raw CSV is not committed — put it in
`data/raw/` (the default name in `src/config.py` is
`heart_failure_readmission_dataset.csv`).

| Group | Columns |
|---|---|
| Identifier (dropped) | `patient_id` |
| Clinical | age, bmi, bnp, sodium, creatinine, systolic_bp, heart_rate |
| Treatment | ace_inhibitor, beta_blocker, diuretic |
| Other | gender, income_level, adherence_score, distance_to_hospital_km |
| Target | `readmitted_30d` (41% positive) |

Data quality notes: `bmi`, `sodium` and `creatinine` are ~3% missing, and
`creatinine` has some impossible negative values. `src/data/clean.py` turns
out-of-range readings into NaN and the modeling pipeline imputes them.

## Structure

```
.
├── data/
│   ├── raw/                  # raw CSV goes here (untracked)
│   ├── interim/
│   └── processed/            # cleaned.csv written by notebook 01
├── notebooks/
│   ├── 01_cleaning.ipynb
│   ├── 02_eda_cleaned.ipynb
│   ├── 03_statistical_testing.ipynb
│   ├── 04_modeling.ipynb
│   ├── 04c_modeling_hgbc.ipynb
│   └── 05_eda_detailed_cleaned.ipynb
├── src/
│   ├── config.py             # paths, constants, seed
│   ├── data/                 # load, clean
│   ├── features/             # preprocessing pipeline
│   ├── models/               # models + evaluation
│   └── viz/                  # plot helpers
├── tests/                    # pytest tests for src/
├── reports/
│   ├── figures/              # generated charts
│   └── tables/               # generated tables
├── models/
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# put the Kaggle CSV at data/raw/heart_failure_readmission_dataset.csv
```

The notebooks add the project root to `sys.path`, so `from src... import ...`
works without installing the package.

## Running

```bash
jupyter notebook
```

Run the notebooks in order:

| # | Notebook | What it does |
|---|---|---|
| 01 | `01_cleaning.ipynb` | preserve the raw data, remove `patient_id`, validate categories/binary fields, flag clinically impossible values, summarize missingness, and save `data/processed/cleaned.csv` |
| 02 | `02_eda_cleaned.ipynb` | run EDA on the cleaned dataset: distributions, missingness, correlations, target comparisons, outlier review, and encoding preview |
| 03 | `03_statistical_testing.ipynb` | run chi-square tests, t-tests / Mann-Whitney tests, effect sizes, odds ratios, multiple-testing correction, and permutation testing |
| 04 | `04_modeling.ipynb` | train and evaluate the majority-class baseline and Logistic Regression pipeline, including metrics, cross-validation, curves, threshold review, and coefficient interpretation |
| 04c | `04c_modeling_hgbc.ipynb` | train and evaluate HistGradientBoosting on the same split and preprocessing as 04, with small AUROC-scored tuning, threshold review, permutation importance, and partial dependence |
| 05 | `05_eda_detailed_cleaned.ipynb` | supplemental cleaned-data EDA: distribution fits, empirical rule, CLT, bootstrap analysis, and Bayesian estimate |

Figures and tables are written to `reports/figures/` and `reports/tables/`.

## Testing

```bash
pytest
```

## Notes

- Run `01_cleaning.ipynb` first. All later notebooks use `data/processed/cleaned.csv` so EDA, statistical testing, and modeling are based on the same validated dataset.
- Modeling (`04`) now includes a majority-class baseline and Logistic Regression workflow. Additional model notebooks/sections can reuse the same cleaned dataset, split, and evaluation metrics for fair comparison.
- The Logistic Regression threshold sweep is performed on a validation split from the training data. The held-out test set is used only for final reported metrics.
- `RANDOM_STATE` in `src/config.py` is there for reproducibility.
- This is coursework on observational data, so results are associations, not causal effects, and are not meant for real clinical use.

## References

- University of San Diego, AAI-500 *Probability and Statistics for AI*.
- Kaggle — *Heart Failure Readmission and Social Determinants of Health* dataset.
- scikit-learn, pandas, statsmodels, scipy docs.
