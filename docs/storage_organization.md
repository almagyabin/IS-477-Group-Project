# Storage and Organization look again

Project Folder Structure:

project/
  data/
    raw/              # downloaded Kaggle files
    processed/        # merged + cleaned files
  db/                 # SQLite database
  results/            # plots and result files
  src/                # Python scripts and workflow files
  docs/               # documentation
  env/                # requirements and environment files

Naming Conventions:
- All raw data uses original Kaggle filenames.
- All processed files are stored as .parquet.
- Workflow outputs are stored in results/.
