# Data Integration

We integrate the two datasets using:
- anime.csv → mal_id
- anime_full_data.json → anime_id

Join Type: Inner join

Conceptual Model:
AnimeCore(mal_id, title, score, favorites, ...)
AnimeFull(anime_id, title_english, genres, year, ...)

Relationship:
AnimeCore.mal_id = AnimeFull.anime_id

The integrated file is stored at:
data/processed/anime_merged.parquet
