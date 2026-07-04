"""
Task 2: Data Processing
Combines the three daily sales CSV files, filters to Pink Morsel only,
computes a `Sales` field (price * quantity), and writes a single
output CSV with the columns: Sales, Date, Region.
"""

import glob
import pandas as pd

# Grab all the daily sales CSV files in the data folder
input_files = glob.glob("data/daily_sales_data_*.csv")

# Read and combine them all into a single DataFrame
all_data = pd.concat((pd.read_csv(f) for f in input_files), ignore_index=True)

# Keep only Pink Morsel rows (case-insensitive, just in case)
pink_morsel_data = all_data[all_data["product"].str.lower() == "pink morsel"].copy()

# Clean the price field (strip "$") and convert to float
pink_morsel_data["price"] = (
    pink_morsel_data["price"].replace(r"[\$,]", "", regex=True).astype(float)
)

# Compute Sales = price * quantity
pink_morsel_data["Sales"] = pink_morsel_data["price"] * pink_morsel_data["quantity"]

# Rename columns to match required output naming
pink_morsel_data = pink_morsel_data.rename(
    columns={"date": "Date", "region": "Region"}
)

# Keep only the three required fields, in order
output_data = pink_morsel_data[["Sales", "Date", "Region"]]

# Sort by date for tidiness
output_data = output_data.sort_values("Date")

# Write the final output
output_data.to_csv("data/formatted_sales_data.csv", index=False)

print(f"Wrote {len(output_data)} rows to data/formatted_sales_data.csv")