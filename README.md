# Bachelor Thesis - IOTA Wealth Distribution

This repository contains the code, data, and analysis files for the Bachelor Thesis about the IOTA wealth distribution. The project focuses on analyzing the wealth distribution within the IOTA ecosystem, especially after the transition to the UTXO model.

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
```

##### Key Files Explanation

- **Data_Cleaning&Data_Preparing.ipynb**: Jupyter notebook used to clean and prepare the dataset for analysis.
- **Database_Creating.ipynb**: Creates the SQLite database (`iotaDB.db`) from raw CSV files.
- **Discriptive_Analysis.ipynb**: Conducts exploratory data analysis on wealth distribution.
- **Gini_Nakamoto_Analysis.ipynb**: Analyzes wealth inequality using Gini and Nakamoto coefficients.
- **IOTA_Wealth_Distribution_Table.csv**: Contains wealth distribution table.

##### Usage

- **Clone the repository**:

    ```bash
    git clone https://github.com/your_username/bachelor_thesis_2024.git
    cd bachelor_thesis_2024
    ```

- **Install the required packages**:

    ```bash
    pip install numpy pandas matplotlib seaborn sqlite3 prettytable json
    ```

- **Run the database creation script**: 
    Execute the `Database_Creating.ipynb` notebook to generate the `iotaDB.db` file.

- **Run analysis notebooks**: 
    Once the database has been created, you can run any of the analysis notebooks.


