from pathlib import Path

import joblib
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_FILE = ROOT / "outputs" / "lightgbm_model.joblib"


def predict(input_data):
    if not MODEL_FILE.exists():
        raise FileNotFoundError(
            "Model artifact not found. Run `python src/train_model.py` first."
        )
    bundle = joblib.load(MODEL_FILE)
    features = bundle["features"]
    frame = pd.DataFrame(input_data)[features]
    prepared = pd.DataFrame(
        bundle["imputer"].transform(frame), columns=features, index=frame.index
    )
    return bundle["model"].predict(prepared)
