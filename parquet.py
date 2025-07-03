import glob
import pandas as pd

files = glob.glob('data/*csv')

for file in files:
    df = pd.read_csv(file)
    # Save the DataFrame to a Parquet file
    parquet_file = file.replace('.csv', '.parquet')
    df.to_parquet(parquet_file,)
