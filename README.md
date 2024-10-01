# Bachelor Thesis 2024 - IOTA Wealth Distribution

This repository contains the code, data, and analysis files for the Bachelor Thesis 2024. The project focuses on analyzing the wealth distribution within the IOTA ecosystem, especially after the transition to the UTXO model.

## Requirements

To execute the scripts and notebooks in this repository, ensure you have the following Python libraries installed:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `sqlite3`
- `ast`
- `prettytable`
- `json`
- `matplotlib.pyplot`

### Install Dependencies

Run the following command to install all the necessary Python packages:

```bash
pip install numpy pandas matplotlib seaborn sqlite3 prettytable json


#### Project Structure


The project is organized into the following main directories and files:

├── Api_Analysis/
│   ├── API_REQUEST_LIST.py
│   ├── API_Richest_Address.py
│   ├── Comparison_Balances_APIvsData.ipynb
│   └── ...
├── Data_Cleaning&Discriptive_Analysis/
│   ├── Data_Cleaning&Data_Preparing.ipynb
│   ├── Discriptive_Analysis.ipynb
│   ├── Database_Creating.ipynb
│   ├── IOTA_1year_tx_data2.csv
│   └── IOTA_Wealth_Distribution_Table.csv
├── Results/
│   ├── Gini_Nakamoto_Analysis.ipynb
│   └── IOTA_1year_tx_data2.csv
├── IOTA_Dataset/
│   ├── iotaDB.db
│   └── ...
├── Git_LFS/
├── Graphical_Representation/
├── RemoteAccess/
└── .gitattributes
Key Files
1. API Analysis
API_REQUEST_LIST.py: Contains functions to fetch IOTA data using APIs.
API_Richest_Address.py: Retrieves the richest addresses within IOTA.
Comparison_Balances_APIvsData.ipynb: Compares balances from the API to the dataset.
