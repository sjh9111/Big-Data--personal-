from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "C:\Users\samjh_000\"
data_dir = "Dropbox\Duke\2014-15\Spring 2015\PUBPOL 590S Big Data\Data"
git_dir = "Documents\GitHub\Big-Data--personal-"

csv file = main_dir + data_dir

df = pd.read_csv(os.path.join(main_dir, csv_file))