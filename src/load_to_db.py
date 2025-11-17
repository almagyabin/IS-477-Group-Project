import sqlite3
import pandas as pd
from pathlib import Path

if __name__ == "__main__":
    db_dir = Path("db")
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / "anime.db"

    conn = sqlite3.connect(db_path)

    anime = pd.read_csv("data/raw/anime.csv")
    anime_full = pd.read_json("data/raw/anime_full_data.json")

    anime.to_sql("anime", conn, if_exists="replace", index=False)
    anime_full.to_sql("anime_full", conn, if_exists="replace", index=False)

    conn.close()
