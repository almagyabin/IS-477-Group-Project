# Data Acquisition

We use two anime datasets from Kaggle:

1. Anime CSV  
   Original Source: https://www.kaggle.com/datasets/vishalkalathil/anime-offline-database/data  
   Filename: anime.csv  
   SHA-256: acb302f9e3328477a0ce438b986dd910629971433271ad37593ae9672a99601e

2. Anime Full JSON  
   Original Source: https://huggingface.co/datasets/realoperator42/anime-titles-dataset  
   Filename: anime_full_data.json  
   SHA-256: 94f2886883c929ea02e745b576ba1403e46bd371f4d0f719339fe38d07052384

3. This the Output Folder link: https://uofi.box.com/s/6xhwtdmpfmuls4nwk0p22mlpwoe0hubq

To Reproduce:
1. Download both files from this Box link: https://uofi.box.com/s/3pe0ahrmk3szcoq81rr4a8xawknadyzu
2. Save them into: data/raw/
3. Your folder structure should look like:
   - data/raw/anime.csv
   - data/raw/anime_full_data.json
4. Verify the integrity of each file by comparing its SHA-256 checksum with the values listed above.
5. Once the data is in place, run the full workflow:
   - Command: snakemake -j 1

6. This will execute all pipeline steps and generate the processed datasets and visual outputs.
