import sqlite3
import serial
import threading
import schedule
import time
import requests
import re

# Function to read and insert data into the database
def read_and_insert_data():
    ser = serial.Serial('COM21', 9600)  # Adjust the COM port and baud rate as needed

    # Create a new database connection and cursor within this thread
    conn_thread = sqlite3.connect('health_data.db')
    cursor_thread = conn_thread.cursor()
    i = 0
    while i<50:
        i = i+1
        data = ser.readline().decode().strip()

        # Extract heart_rate and temperature values from the data using regular expressions
        match = re.search(r'heart_rate=(\d+\.\d+)&temperature=(\d+\.\d+)', data)

        if match:
            heart_rate, temperature = map(float, match.groups())

            cursor_thread.execute("INSERT INTO records (heart_rate, temperature, status) VALUES (?, ?, 0)", (heart_rate, temperature))
            conn_thread.commit()

    ser.close()
    # Close the database connection at the end of the thread
    conn_thread.close()

# Create a thread for the data reading loop
data_thread = threading.Thread(target=read_and_insert_data)

# Start the data thread
data_thread.start()

# Connect to the SQLite database
conn = sqlite3.connect('health_data.db')
cursor = conn.cursor()

# Create the "records" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        heart_rate REAL,
        temperature REAL,
        status INTEGER DEFAULT 0
    )
''')
conn.commit()

# Function to upload pending records to a web server
def upload_data():
    # Fetch records with status 0 (not uploaded)
    cursor.execute("SELECT * FROM records WHERE status = 0")
    records = cursor.fetchall()

    if records:
        for record in records:
            record_id, timestamp, heart_rate, temperature, _ = record
            # Simulate the upload process by sending data to a web server
            upload_success = upload_to_server(record_id, timestamp, heart_rate, temperature)

            if upload_success:
                # Update the status to 1 for the successfully uploaded record
                cursor.execute("UPDATE records SET status = 1 WHERE id = ?", (record_id,))
                conn.commit()

# Function to simulate uploading data to a web server
def upload_to_server(record_id, timestamp, heart_rate, temperature):
    # Replace this with actual code to upload data to your web server
    try:
        # Simulate a successful upload
        response = requests.post('https://example.com/upload', json={'timestamp': timestamp, 'heart_rate': heart_rate, 'temperature': temperature})
        if response.status_code == 200:
            print(f"Record {record_id} uploaded successfully.")
            return True
    except Exception as e:
        # Handle any exceptions or errors during the upload process
        print(f"Failed to upload record {record_id}: {str(e)}")
    return False


# Schedule the upload_data function to run every minute
schedule.every(1).minutes.do(upload_data)

# Your other application logic can run here alongside the data reading loop and the cron job
read_and_insert_data()
while True:
    schedule.run_pending()
    time.sleep(1)

# Close the serial port and the database connection when done (if needed)
# conn.close()
