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
    try:
        import requests
    except ImportError:
        print("ERROR: requests package not installed.", file=sys.stderr)
        return False

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


def download_kaggle_csv(dest_dir: Path) -> bool:
    """
    Attempt to download the anime CSV via Kaggle API.
    Returns True if anime-dataset-2025.csv exists at the end, False otherwise.
    """
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        print("Kaggle API not installed. Skipping Kaggle download.", file=sys.stderr)
        return False

    api = KaggleApi()
    try:
        api.authenticate()
    except Exception as e:
        print("Failed to authenticate with Kaggle. Skipping Kaggle download.", file=sys.stderr)
        print(e, file=sys.stderr)
        return False

    print("Attempting Kaggle API download for anime-dataset-2025.csv ...")
    print("Dataset URL: https://www.kaggle.com/datasets/rafidahmed816/anime-dataset-2025")

    try:
        api.dataset_download_file(
            "rafidahmed816/anime-dataset-2025",  # dataset id (adjust if needed)
            "anime-dataset-2025.csv",            # file name inside dataset
            path=str(dest_dir),
            force=True,
        )
    except Exception as e:
        print("Kaggle API download failed. This is expected if the file or dataset name is different.", file=sys.stderr)
        print(e, file=sys.stderr)
        return False

    csv_path = dest_dir / "anime-dataset-2025.csv"
    zip_path = dest_dir / "anime-dataset-2025.csv.zip"

    # If Kaggle created a .zip, extract it
    if zip_path.exists() and not csv_path.exists():
        import zipfile
        print("Extracting anime-dataset-2025.csv from zip...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extract("anime-dataset-2025.csv", dest_dir)
        zip_path.unlink()

    return csv_path.exists()


if __name__ == "__main__":
    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)

    # filenames used in the project
    anime_csv_path = data_dir / "anime-dataset-2025.csv"
    anime_json_path = data_dir / "anime_full_data.json"

    csv_exists = anime_csv_path.exists()
    json_exists = anime_json_path.exists()

    # Try Kaggle for the CSV if it doesn't exist yet
    if not csv_exists:
        csv_exists = download_kaggle_csv(data_dir)

    # Try HuggingFace for the JSON if it doesn't exist yet
    if not json_exists:
        hf_url = (
            "https://huggingface.co/datasets/realoperator42/anime-titles-dataset/"
            "resolve/main/anime_full_data.json"
        )
        json_exists = download_hf_json(hf_url, anime_json_path)

    missing = []
    if not csv_exists:
        missing.append("anime-dataset-2025.csv")
    if not json_exists:
        missing.append("anime_full_data.json")

    if missing:
        print("\nThe following files are missing and could not be downloaded automatically:")
        for f in missing:
            print(" -", f)
        print("\nPlease download these files from Box and place them in data/raw/")
        sys.exit(1)

    # Print SHA-256 hashes for documentation
    print("anime-dataset-2025.csv SHA-256:", sha256_checksum(anime_csv_path))
    print("anime_full_data.json SHA-256:", sha256_checksum(anime_json_path))
