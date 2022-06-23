#!/usr/bin/python3
import pandas as pd
import sys
df = pd.read_parquet(sys.argv[1])
df.to_csv('filename.csv')
print(sys.argv[1])