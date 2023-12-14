# This file is meant to read data from sqlite3 and display the first 20 records.
import sqlite3

cursor = sqlite3.connect("data.db").cursor()
cursor.execute("SELECT * FROM health_table_tbl")
rows = cursor.fetchall()

i = 0
for row in rows:
    if i > 20:
        break
    print(row)
    i = i+1