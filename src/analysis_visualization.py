import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

if __name__ == "__main__":
    processed_dir = Path("data/processed")
    results_dir = Path("results")
    results_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_parquet(processed_dir / "anime_clean.parquet")

    rating_counts = df["score_csv"].value_counts().sort_index()
    rating_counts.to_csv(processed_dir / "rating_counts.csv", index=True)

    plt.figure()
    rating_counts.plot(kind="bar")
    plt.xlabel("User score")
    plt.ylabel("Count of anime")
    plt.title("Distribution of user scores")
    plt.tight_layout()
    plt.savefig(results_dir / "rating_distribution.png")

    plt.figure()
    plt.scatter(df["score_csv"], df["favorites"])
    plt.xlabel("User score")
    plt.ylabel("Favorites")
    plt.title("User score vs. Favorites")
    plt.tight_layout()
    plt.savefig(results_dir / "rating_vs_favorites.png")

    corr = df[["score_csv", "favorites"]].corr().loc["score_csv", "favorites"]
    with open(results_dir / "correlation.txt", "w") as f:
        f.write(str(corr))

