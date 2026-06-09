from pathlib import Path

import openpyxl
import pandas as pd

d_raw = pd.read_excel('C:/Projects/SHAPE/data/raw/Test O_G_Equipment_Data.xlsx')

print(d_raw.head())