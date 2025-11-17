import pandas as pd
from pathlib import Path

if __name__ == "__main__":
    anime = pd.read_csv("data/raw/anime.csv")
    anime_full = pd.read_json("data/raw/anime_full_data.json")

    merged = anime.merge(
        anime_full,
        left_on="mal_id",
        right_on="anime_id",
        suffixes=("_csv", "_json")
    )

    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)

    merged.to_parquet(processed_dir / "anime_merged.parquet", index=False)
