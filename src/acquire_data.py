# Code by Obi (Week 7). Summary: downloads raw anime datasets and computes SHA-256 checksums.

# File: src/acquire_data.py
# Code by Obi (Week 7). Summary: acquires raw data from Kaggle/HuggingFace when needed, or verifies existing files and prints SHA-256.

import hashlib
from pathlib import Path
import sys


def sha256_checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def download_hf_json(url: str, dest: Path) -> bool:
    try:
        import requests
    except ImportError:
        print("requests is not installed. Install it with: pip install requests", file=sys.stderr)
        return False

    print(f"Downloading HuggingFace JSON from {url} ...")
    resp = requests.get(url, stream=True)
    if resp.status_code != 200:
        print(f"Failed to download JSON from HuggingFace. Status code: {resp.status_code}", file=sys.stderr)
        return False

    with dest.open("wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return True


def download_kaggle_csv(dest_dir: Path) -> bool:
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        print("Kaggle API is not installed. Install it with: pip install kaggle", file=sys.stderr)
        return False

    api = KaggleApi()
    try:
        api.authenticate()
    except Exception as e:
        print("Failed to authenticate Kaggle API. Make sure kaggle.json is configured in ~/.kaggle.", file=sys.stderr)
        print(e, file=sys.stderr)
        return False

    print("Downloading anime.csv from Kaggle using Kaggle API ...")
    # Dataset: vishalkalathil/anime-offline-database, file: anime.csv
    api.dataset_download_file(
        "vishalkalathil/anime-offline-database",
        "anime.csv",
        path=str(dest_dir),
        force=True,
    )

    csv_path = dest_dir / "anime.csv"
    zip_path = dest_dir / "anime.csv.zip"

    # In some cases Kaggle may create a .zip file; handle that too.
    if zip_path.exists() and not csv_path.exists():
        import zipfile

        print("Extracting anime.csv from anime.csv.zip ...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extract("anime.csv", dest_dir)
        zip_path.unlink()

    if not csv_path.exists():
        print("anime.csv was not found after Kaggle download.", file=sys.stderr)
        return False

    return True


if __name__ == "__main__":
    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)

    anime_csv_path = data_dir / "anime.csv"
    anime_json_path = data_dir / "anime_full_data.json"

    # 1. If files already exist (e.g., downloaded from Box), just verify and print hashes.
    csv_exists = anime_csv_path.exists()
    json_exists = anime_json_path.exists()

    if not csv_exists:
        # Try to download from Kaggle using the Kaggle API.
        csv_exists = download_kaggle_csv(data_dir)

    if not json_exists:
        # Try to download JSON directly from HuggingFace.
        hf_url = (
            "https://huggingface.co/datasets/realoperator42/anime-titles-dataset/"
            "resolve/main/anime_full_data.json"
        )
        json_exists = download_hf_json(hf_url, anime_json_path)

    # If still missing, give a clear message and fail.
    missing = []
    if not csv_exists:
        missing.append("anime.csv")
    if not json_exists:
        missing.append("anime_full_data.json")

    if missing:
        print("The following raw data files are missing and could not be downloaded programmatically:")
        for name in missing:
            print(" -", name)
        print("\nPlease download these files from Box and place them in data/raw/ before running the workflow.")
        sys.exit(1)

    # Compute and print SHA-256 checksums for documentation.
    print("anime.csv SHA-256:", sha256_checksum(anime_csv_path))
    print("anime_full_data.json SHA-256:", sha256_checksum(anime_json_path))
