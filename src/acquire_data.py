# Code by Obi (Week 7). Summary: downloads raw anime datasets and computes SHA-256 checksums.

import hashlib
import requests
import hashlib
from pathlib import Path
import sys

def sha256_checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)

    anime_csv_path = data_dir / "anime.csv"
    anime_json_path = data_dir / "anime_full_data.json"

    # Check that files already exist (downloaded manually from Box / Kaggle)
    missing = []
    if not anime_csv_path.exists():
        missing.append("anime.csv")
    if not anime_json_path.exists():
        missing.append("anime_full_data.json")

    if missing:
        print("The following raw data files are missing in data/raw/:")
        for name in missing:
            print(" -", name)
        print("\nPlease download these files from Box and place them in data/raw/ before running the workflow.")
        sys.exit(1)

    print("anime.csv SHA-256:", sha256_checksum(anime_csv_path))
    print("anime_full_data.json SHA-256:", sha256_checksum(anime_json_path))
