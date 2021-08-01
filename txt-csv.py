import csv
import pandas as pd

read_file = pd.read_csv (r'test.txt')
read_file.to_csv (r'test.csv', index=None)
