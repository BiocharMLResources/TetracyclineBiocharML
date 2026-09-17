from pathlib import Path

import joblib
import pandas as pd
from lightgbm import LGBMRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "data.xlsx"
MODEL_FILE = ROOT / "outputs" / "lightgbm_model.joblib"

FEATURES = [
    "Pyro_T", "Pyro_time", "SSA", "PV", "pore_size", "C_pct", "H_pct",
    "O_pct", "N_pct", "HC", "OC", "ONC", "pHpzc", "Ads_temp",
    "rotation", "contact_time", "pH", "C0", "dosage",
]
TARGET = "TC_removal_efficiency_pct"
RANDOM_STATE = 92

PARAMETERS = {
    "boosting_type": "gbdt",
    "colsample_bytree": 1.0,
    "learning_rate": 0.3,
    "max_depth": 3,
    "min_child_samples": 5,
    "min_child_weight": 0.001,
    "min_split_gain": 0.0,
    "n_estimators": 771,
    "n_jobs": 1,
    "num_leaves": 227,
    "reg_alpha": 0.0,
    "reg_lambda": 0.0,
    "subsample": 1.0,
    "subsample_for_bin": 200000,
    "subsample_freq": 0,
    "verbose": -1,
    "random_state": RANDOM_STATE,
}


def main():
    data = pd.read_excel(DATA_FILE, sheet_name="Data")
    x_train, x_test, y_train, y_test = train_test_split(
        data[FEATURES],
        data[TARGET],
        test_size=0.20,
        random_state=RANDOM_STATE,
        shuffle=True,
    )

    imputer = SimpleImputer(strategy="median")
    x_train_ready = pd.DataFrame(
        imputer.fit_transform(x_train), columns=FEATURES, index=x_train.index
    )
    x_test_ready = pd.DataFrame(
        imputer.transform(x_test), columns=FEATURES, index=x_test.index
    )

    model = LGBMRegressor(**PARAMETERS)
    model.fit(x_train_ready, y_train)
    predictions = model.predict(x_test_ready)

    print(f"R2: {r2_score(y_test, predictions):.6f}")
    print(f"RMSE: {mean_squared_error(y_test, predictions) ** 0.5:.6f}")
    print(f"MAE: {mean_absolute_error(y_test, predictions):.6f}")

    MODEL_FILE.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {"model": model, "imputer": imputer, "features": FEATURES},
        MODEL_FILE,
    )


if __name__ == "__main__":
    main()
