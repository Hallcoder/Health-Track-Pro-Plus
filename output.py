import csv

# Function to extract systolic pressure from blood pressure string
def extract_systolic(bp_string):
    return bp_string.split('/')[0]

# Input and output file paths
input_csv = 'data.csv'  # Replace with your input CSV file path
output_csv = 'output_data.csv'  # Replace with your desired output CSV file path

# Open input CSV file and create output CSV file
with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    print(fieldnames)
    # Modify fieldnames to update 'blood_pressure' to 'systolic_pressure'
    fieldnames[fieldnames.index('blood pressure')] = 'systolic_pressure'

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    # Process each row and update 'systolic_pressure' column
    for row in reader:
        row['systolic_pressure'] = extract_systolic(row['blood pressure'])
        del row['blood pressure']  # Remove 'blood_pressure' column

        # Write modified row to output file
        writer.writerow(row)

print("Conversion completed. Output saved to:", output_csv)
