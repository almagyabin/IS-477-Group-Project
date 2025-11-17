# **INTERIM STATUS REPORT**

## **Project Overview and Current Status**

Our project aims to analyze two anime datasets sourced from Kaggle to answer two core research questions: <ins>What is the most common user rating score assigned to anime?</ins> and <ins>Does a higher rating correlate with having more favorites?</ins>

We integrate two distinct datasets, anime.csv and anime_full_data.json, which differ in format, schema, and field structure. One dataset (CSV) contains core information such as title, popularity, and numerical score, while the second dataset (JSON) includes more detailed information such as genres, year, themes, studios, and metadata. This ensures we meet the course requirement of acquiring data from two different formats with differing schemas. At this stage, our project is on schedule and nearly all technical tasks associated with data acquisition, storage, cleaning, integration, analysis, and workflow automation have been completed. We have successfully built a complete end-to-end automated pipeline using Snakemake, and our processing scripts generate merged datasets, cleaned datasets, visualizations, and summary statistics that directly answer both research questions. The majority of our coding artifacts, including acquisition scripts, integration scripts, cleaning scripts, analysis scripts, and workflow files, have been completed and are already present in the repository under the src/ directory. The processed outputs (anime_merged.parquet, anime_clean.parquet) as well as the visualizations (rating_distribution.png and rating_vs_favorites.png) are also automatically generated in the correct folders once the workflow is executed. A small caveat is that the code may not generate any outputs because we were not able to properly upload our data as some of the files were too large. We are currently focusing on completing documentation, metadata, and reproducibility artifacts required by the course.

## **Progress Update by Project Task**

Below is an update on each major task outlined in our project plan, along with references to specific artifacts now stored in our GitHub repository.

### **Data Collection and Acquisition**

We obtained two different datasets from Kaggle (one CSV and one JSON) to meet Milestone 2 feedback requiring diversity in file formats. The JSON dataset was uploaded to GitHub because it is below 25MB, while the CSV dataset (31.8MB) exceeded GitHub’s file size limit and was therefore placed in Box. Our documentation will instruct users to download the raw datasets from Box and place them into data/raw/. The acquire_data.py script (created by Obi) includes checksum generation and can optionally automate downloading once Kaggle URLs and access tokens are configured. SHA-256 hashes have been generated and will be added to the documentation in the next milestone.

### **Storage and Organization**

We established a structured directory layout aligned with best practices from the course, including separate directories for raw data, processed data, scripts, workflows, results, and metadata. Our scripts automatically generate the data/processed/ and results/ folders if they do not exist.

### **Data Integration**

Integration required mapping mal_id from the CSV dataset to anime_id from the JSON dataset. Alma completed the integration script using pandas, producing a merged dataset with more than 80 combined attributes. The integration logic has been validated and works correctly.

### **Data Quality Assessment and Cleaning**

The cleaning process (handled by Obi) included converting rating-related fields to numeric values, removing missing entries, dropping out-of-range scores, and ensuring consistency in key variables. The finalized cleaned dataset contains 999 valid records. Outliers were inspected and handled appropriately. Cleaning documentation will be finalized next.


### **Exploratory Data Analysis & Visualization**

Alma completed the analysis step by generating summary statistics and visualizations to answer both research questions. Findings so far show that *the most common user rating score is 7.55* and *there is a moderate positive correlation (~0.40) between rating score and favorites.* These visual outputs are automatically generated and stored under results/ when we upload the data.

### **Workflow Automation and Provenance**

Obi set up a complete Snakemake pipeline that automates the entire lifecycle: from acquisition to visualization. Running run_all.py triggers the entire workflow, making the project fully reproducible. This satisfies the provenance requirement of Modules 11–12.

### **Reproducibility and Transparency Artifacts**

We still need to assemble the supporting documentation and metadata. This includes environment files (pip_freeze.txt), a full reproducibility guide, data dictionary, metadata schema, and license selection.

### **Metadata and Data Documentation**

Documentation will include a data dictionary describing variables from both datasets, along with DataCite or Schema.org metadata about the project. We are on schedule, with all major technical components complete. Remaining work includes documentation, metadata, licenses, and preparing our final deliverable materials.

## **Changes Since Milestone 2**

A few key changes were made to improve alignment with course expectations. Based on the previous feedback we recieved, we replaced one of the CSV files with a JSON dataset to ensure the two source datasets differ in structure and format. Due to GitHub’s 25MB limit, we now store anime.csv in Box and instruct users to download it into data/raw/. This follows project guidelines and ensures reproducibility. The Snakemake workflow was expanded to handle acquisition, integration, cleaning, analysis, and visualization, which will ensure full end-to-end reproducibility. After exploring the schema, we confirmed the integration key is mal_id (CSV) ↔ anime_id (JSON). No major deviations from the project’s original goals have been necessary. We remain on schedule and confident in our progress.

## **Individual Contributions and Summary**

### **Obi’s Contributions**

Obi led the development of backend data-processing scripts, including acquire_data.py (for checksums and acquisition), quality_cleaning.py (complete data cleaning logic), and most of the workflow automation work (Snakefile and run_all.py). Obi also handled the integration troubleshooting, file-size limitations, and Box-based data storage solution. Additionally, Obi tested the full pipeline and validated that all scripts function as intended when executed locally. Obi coordinated the organization of the project structure in GitHub, created the directories, and ensured that the processing pipeline adheres to the course requirements. Throughout Milestone 3, Obi ensured the code was consistent, reproducible, and properly aligned with class expectations.

### **Alma’s Contributions**

Alma implemented the dataset integration via integrate_data.py, constructed the SQLite database loader (load_to_db.py), and developed the full analysis and visualization script (analysis_visualization.py). Alma handled the merging of the CSV and JSON datasets, validated the integrated schema, and produced the concept model mapping for documentation. Alma created the bar chart showing the distribution of user scores, the scatter plot showing the relationship between scores and favorites, and the correlation summary. Alma also contributed to shaping the metadata and documentation structure, prepared the data dictionary draft, and worked on the interpretive portions of the analysis. Alma coordinated dataset selection and helped update the project plan based on Milestone 2 feedback.

### **Summary**

In conclusion, nearly all major coding components are completed, including data integration, cleaning, analysis, visualization, and workflow automation. Our datasets have been successfully acquired, processed, and analyzed. The remaining tasks involve writing documentation, metadata, and final deliverables for full reproducibility. The team is working effectively together, with clear division of responsibilities and consistent weekly progress. We expect to fully meet the final project requirements before the deadline.
