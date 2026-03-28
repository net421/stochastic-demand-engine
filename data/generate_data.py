import pandas as pd
import numpy as np

def generate_store_data(n_days=180, seed=42):
    np.random.seed(seed)

    data = pd.DataFrame({
        "date": pd.date_range(start="2025-01-01", periods=n_days, freq="D"),
    })

    data["day_of_week"] = data["date"].dt.dayofweek

    base_lambda = 20
    seasonal_effect = data["day_of_week"].apply(lambda x: 1.3 if x in [4,5] else 0.8)

    data["customers"] = np.random.poisson(base_lambda * seasonal_effect)
    data["service_rate"] = np.random.uniform(22, 30, size=n_days)

    conversion_rate = 0.7
    data["sales"] = np.random.binomial(data["customers"], conversion_rate)

    return data

if __name__ == "__main__":
    df = generate_store_data()
    df.to_csv("store_data.csv", index=False)
