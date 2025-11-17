
# Workflow and Reproducibility

To reproduce the entire pipeline:

1. Install Python 3.10+
2. Install dependencies:
   pip install -r env/requirements.txt
3. Download input data from Box and place into data/raw/
4. Run the workflow:
   python src/workflow/run_all.py

The Snakemake pipeline automates:
- Acquisition
- Loading into database
- Integration
- Cleaning
- Analysis
- Visualization

All results are generated in the results/ folder.
