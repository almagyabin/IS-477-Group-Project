
# Workflow and Reproducibility

To reproduce the entire pipeline:

1. Install Python 3.10+
2. Install dependencies:
   pip install -r env/requirements.txt
3. Download input data from Box and place into data/raw/ (this only needs to be done for the csv, the hugging face json is automated)
4. Run the workflow:
   python src/workflow/run_all.py

The Snakemake pipeline automates:
- Acquisition (only hugging face json is automated, CSV needs to be downloaded from Box)
- Loading into database
- Integration
- Cleaning
- Analysis
- Visualization

All results are generated in the results/ folder.
