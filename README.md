# Tetracycline removal by biochar: machine-learning resources

This repository provides the processed modeling dataset and supporting code associated with the study on machine-learning prediction of tetracycline removal by biochar.

## Contents

- Processed modeling dataset
- Data dictionary
- Model training and prediction code

Pretrained model weights are not distributed. Running the training script
reconstructs the model locally and writes the generated artifact to the ignored
`outputs/` directory.

## Data

The dataset contains 1,044 condition-level records with 19 model input variables and tetracycline removal efficiency (%) as the prediction target.

The released spreadsheet is the numerical model matrix and therefore excludes
bibliographic fields and material names that were not used as model inputs. The
source studies, DOI metadata, reported biochar material names, and each study's
contribution to the final dataset are documented in Supplementary Information
Table S1. The record counts reported in Table S1 reconcile to the 1,044 records
released here. The spreadsheet and Table S1 should therefore be used together
when reviewing data provenance.

Variable definitions and units are provided in `data/DATA_DICTIONARY.md`.

## Reproduce the model

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/train_model.py
```

The training script prints the fixed-split evaluation metrics and creates
`outputs/lightgbm_model.joblib`. Generated model files are intentionally ignored
by version control and are not part of this repository.

## Limitations

The dataset was compiled from heterogeneous literature sources and does not fully represent all water-chemistry conditions, biochar compositions, or engineered biochar systems. Model outputs are intended for preliminary screening and scenario exploration and should not be considered a substitute for experimental validation.

## License and citation

The code is released under the MIT License.

Citation information will be updated after publication.
