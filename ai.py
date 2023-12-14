import csv
import sqlite3
import os

# Function to read CSV and insert into SQLite database
def csv_to_sqlite(csv_file, db_file, table_name):
    # Check if the database file exists
    if not os.path.exists(db_file):
        conn = sqlite3.connect(db_file)
        conn.close()

    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            cholesterol INTEGER,
            systolic_pressure INTEGER,
            diastolic_pressure INTEGER
        )
    '''.format(table_name))

    # Read data from CSV and insert into the SQLite database
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header if present

        for row in csv_reader:
            # Split blood_pressure into systolic and diastolic pressure
            systolic, diastolic = map(int, row[2].split('/'))
            row[2] = systolic  # Update blood_pressure with systolic value
            row.append(diastolic)  # Add diastolic pressure to the row

            # Insert data into the table
            query = f'INSERT INTO {table_name} (age, cholesterol, systolic_pressure, diastolic_pressure) VALUES (?, ?, ?, ?)'
            cursor.execute(query, row[:4])  # Replace column names with CSV columns

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Usage example
csv_file_path = 'data.csv'  # Replace with your CSV file path
database_file_path = 'data.db'  # Replace with your desired SQLite database file path
table_name = 'health_table_tbl'  # Replace with your table name

csv_to_sqlite(csv_file_path, database_file_path, table_name)
