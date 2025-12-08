# Code by Obi (Week 7). Summary: downloads raw anime datasets and computes SHA-256 checksums.

import hashlib
from pathlib import Path
import sys


def sha256_checksum(path: Path) -> str:
    """Compute SHA-256 checksum for a file."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def download_hf_json(url: str, dest: Path) -> bool:
    """Download public HuggingFace JSON dataset."""
    import requests

    print(f"Downloading HuggingFace JSON from {url} ...")
    resp = requests.get(url, stream=True)
    if resp.status_code != 200:
        print(f"Failed to download JSON. HTTP {resp.status_code}", file=sys.stderr)
        return False

    with dest.open("wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return True


if __name__ == "__main__":
    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)

    anime_csv_path = data_dir / "anime.csv"
    anime_json_path = data_dir / "anime_full_data.json"

    csv_exists = anime_csv_path.exists()
    json_exists = anime_json_path.exists()

    if not csv_exists:
        print(
            "anime.csv is missing.\n"
            "Please download it manually and place it in data/raw/",
            file=sys.stderr,
        )
        sys.exit(1)

    if not json_exists:
        hf_url = (
            "https://huggingface.co/datasets/realoperator42/anime-titles-dataset/"
            "resolve/main/anime_full_data.json"
        )
        json_exists = download_hf_json(hf_url, anime_json_path)

    if not json_exists:
        print(
            "anime_full_data.json is missing and could not be downloaded.\n"
            "Please download it manually and place it in data/raw/",
            file=sys.stderr,
        )
        sys.exit(1)

    print("anime.csv SHA-256:", sha256_checksum(anime_csv_path))
    print("anime_full_data.json SHA-256:", sha256_checksum(anime_json_path))

