# Code by Obi (Weeks 8–9). Summary: cleans user score and favorites and filters invalid values.

import pandas as pd
from pathlib import Path

if __name__ == "__main__":
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_parquet(processed_dir / "anime_merged.parquet")

    df["score_csv"] = pd.to_numeric(df["score_csv"], errors="coerce")
    df["favorites"] = pd.to_numeric(df["favorites"], errors="coerce")

    df = df.dropna(subset=["score_csv", "favorites"])
    df = df[df["score_csv"].between(1, 10)]

    df.to_parquet(processed_dir / "anime_clean.parquet", index=False)
