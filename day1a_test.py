import pandas as pd

# 1. Load Data with Absolute Path
path = r'D:\Industrial_AI_Masters\01_Prerequisites\Python_Analytics\water_potability.csv'
df = pd.read_csv(path)
print("Dataset loaded successfully!")


print("--- Day 1: Practical Execution ---")

# 2. THE "PH FIX": Handle missing sensor data
# Filling NaN with 7.0 (Neutral) - A standard engineering assumption
df['ph'].fillna(7.0)
print("Missing pH values handled.")
# 3. THE "HARDNESS FILTER": Identify high-scaling risk water
# In industry, Hardness > 250 mg/L is often considered 'Very Hard'
high_hardness=df[df['Hardness']>250].head()
print(high_hardness)


# 4. DATA SENSE-CHECK: Range of your parameters
print("\n--- Process Range Check ---")
print(f"Min PH: {df['ph'].min()}")
print(f"Max PH: {df['ph'].max()}")
print(f"Avg Sulfate: {df['Sulfate'].mean()} mg/L")

# 5. Output first 5 rows of the 'High Risk' water for review
print("\nFirst 5 Rows of High Hardness Water:")
print(high_hardness[['ph', 'Hardness', 'Solids']].head())
