from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "C:\Users\samjh_000"
git_dir = "\Documents\GitHub"
#csv_file = "\Dropbox\Duke\YR 2014-15\Spring 2015\PUBPOL 590S Big Data\Data\small_data_w_missing_duplicated.csv"
csv_file = "\Desktop\small_data_w_missing_duplicated.csv"

#Import data    
#df = pd.read_csv(os.path.join(main_dir,csv_file))
df = pd.read_csv(main_dir + csv_file)

# 1.Convert missing data
missing = ['.', 'NA', 'NULL', '', '-']

df = pd.read_csv(main_dir + csv_file, na_values = missing)

# 2. drop full row duplicates
df = df.drop_duplicates()

# 3. Extract only the rows where consumption is missing 
rows = df['consump'].isnull()
df1 = df[rows]

# 4. drop rows w/same Date and Consump AND with missing consump
df2 = df.drop_duplicates(['panid', 'date'])

rows2 = df2['consump'].notnull()
df2 = df2[rows2]

# 5. Take mean of consumption
df2.consump.mean()
    

