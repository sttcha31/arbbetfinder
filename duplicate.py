import pandas as pd

# Read the CSV file
df = pd.read_csv("odds.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Save the cleaned data back to the CSV file
df.to_csv("odds.csv", index=False)