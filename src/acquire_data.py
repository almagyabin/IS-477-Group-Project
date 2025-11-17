# Code by Obi (Week 7). Summary: downloads raw anime datasets and computes SHA-256 checksums.

import hashlib
import requests
from pathlib import Path

def download_file(url: str, dest_path: Path) -> None:
    response = requests.get(url)
    response.raise_for_status()
    dest_path.write_bytes(response.content)

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

    anime_csv_url = "https://kaggle-url-for-anime-csv"
    anime_json_url = "https://kaggle-url-for-anime-json"

    if not anime_csv_path.exists():
        download_file(anime_csv_url, anime_csv_path)

    if not anime_json_path.exists():
        download_file(anime_json_url, anime_json_path)

    print("anime.csv SHA-256:", sha256_checksum(anime_csv_path))
    print("anime_full_data.json SHA-256:", sha256_checksum(anime_json_path))
