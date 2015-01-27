#Sam Hile
#Canopy assignment 1

#import packages
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#Set up file paths
main_dir = "C:\Users\samjh_000\Desktop"
txt_file = "\File1_small.txt"

#Import data into dataframe
df = pd.read_table(main_dir+txt_file, sep = "\s")

##Row slicing
#extract Rows 60-90
df[60:91]

#Extract rows where kWh>30
df[df.kwh > 30]