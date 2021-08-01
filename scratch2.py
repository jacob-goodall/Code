from pathlib import Path
import pandas as pd
import sqlite3
Path('my_data.db').touch()

conn = sqlite3.connect('my_data.db')
c = conn.cursor()

c.execute('''CREATE TABLE crosses (First, Last)''')

# load the data into a Pandas DataFrame
users = pd.read_csv('users.csv')
# write the data to a sqlite table
users.to_sql('users', conn, if_exists='append', index = False)

