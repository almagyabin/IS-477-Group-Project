# Obi Data Quality and Cleaning look again

Quality Checks Performed:
- Verified numeric fields (score_csv, favorites)
- Checked for missing values
- Ensured user scores are between 1 and 10
- Removed rows with corrupted or non-numeric values
- Inspected duplicates based on mal_id

Cleaning Steps:
- Converted score_csv and favorites to numeric
- Dropped rows with missing score or favorites
- Filtered scores outside [1, 10]
- Saved cleaned dataset to:
  data/processed/anime_clean.parquet
