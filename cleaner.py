
import csv


input_file = input("Enter CSV file name: ")

if not input_file.lower().endswith(".csv"):
    print("Error: Please select a CSV file.")
    exit()

output_file = input("Enter output file name: ")

if not output_file.lower().endswith(".csv"):
    if "." in output_file:
        print("Error: Please enter a valid CSV filename.")
        exit()
    output_file += ".csv"

rows = []

# Read CSV file

rows = []

try:
    # Check file extension
    if not input_file.lower().endswith(".csv"):
        print("Error: Please select a CSV file.")
        exit()

    with open(input_file, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)
        headers = reader.fieldnames

        # Check headers
        if not headers or not all(headers):
            print("Error: CSV file has invalid headers.")
            exit()

        # Read data
        for row in reader:
            rows.append(row)

except FileNotFoundError:
    print("Error: File not found.")
    exit()

except PermissionError:
    print("Error: Permission denied.")
    exit()

except UnicodeDecodeError:
    print("Error: Unable to read file encoding.")
    exit()





print("CSV DATA CLEANER")
print("----------------")
print("Total rows:", len(rows))


    
# Find missing values

# Find missing values in each column
missing_count = 0

print("\nMISSING VALUE REPORT")
print("--------------------")

for column in headers:
    column_missing = 0

    for row in rows:
        if row[column] == "":
            column_missing += 1

    missing_count += column_missing

    print(column + ":", column_missing)

print("Total missing values:", missing_count)


# Find duplicate rows
unique_rows = []
seen = set()
duplicate_count = 0

for row in rows:
    row_key = tuple(row[column] for column in headers)

    if row_key in seen:
        duplicate_count += 1
    else:
        seen.add(row_key)
        unique_rows.append(row)

print("Duplicate rows:", duplicate_count)

# Fill missing values
replaced_count = 0
for row in unique_rows:
    for column in headers:
        if row[column] == "":
            row[column] = "Unknown"
            replaced_count += 1



# Save cleaned CSV
with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(unique_rows)

# Final cleaning summary
print("\nFINAL CLEANING SUMMARY")
print("-----------------------")
print("Original rows:", len(rows))
print("Duplicate rows removed:", duplicate_count)
print("Missing values replaced:", replaced_count)
print("Final rows:", len(unique_rows))
print("Output file:", output_file)
print("-----------------------")
print("Data cleaning successful!")


