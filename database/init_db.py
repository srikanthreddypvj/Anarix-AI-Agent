import pandas as pd
import sqlite3

conn = sqlite3.connect('database/ecommerce.db')

dfs = {
    'total_sales': pd.read_csv('data/total_sales.csv'),
    'ad_sales': pd.read_csv('data/ad_sales.csv'),
    'eligibility': pd.read_csv('data/eligibility.csv')
}

for table, df in dfs.items():
    df.to_sql(table, conn, if_exists='replace', index=False)

print("✅ Database created!")
