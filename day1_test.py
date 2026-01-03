import pandas as pd
import numpy as np
import sys
import os
from pathlib import Path

# 1. Environment Check
print(f"--- Environment Check ---")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Pandas Version: {pd.__version__}")
print("-" * 25)

# 2. Load the Dataset 
# Note: Ensure the 'water_potability.csv' is in the same folder as this script
try:
    # Use dynamic path resolution
    script_dir = Path(__file__).parent
    dataset_path = script_dir / 'water_potability.csv'

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found at {dataset_path}")

    df = pd.read_csv(dataset_path)
    print("Success: Dataset loaded correctly!")

    # 3. Quick Industrial Analysis
    print("\n--- Industrial Data Snapshot ---")

    # Validate required columns
    required_columns = ['ph', 'Hardness', 'Solids']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Checking for missing values in pH (Crucial for Solenis/Exxon)
    missing_ph = df['ph'].isnull().sum()
    avg_hardness = df['Hardness'].mean()

    print(f"Missing pH readings: {missing_ph}")
    print(f"Average System Hardness: {avg_hardness:.2f} ppm")
    print("-" * 25)

    # 4. View Top 5 Rows
    print("\nFirst 5 Rows of Plant Data:")
    print(df[['ph', 'Hardness', 'Solids']].head())
    print(df[['Hardness', 'ph']].head(5))

except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}") 

