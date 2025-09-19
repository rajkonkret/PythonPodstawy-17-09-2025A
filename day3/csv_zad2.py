import csv

read_fields = []
read_rows = []

filename = "records.csv"
with open(filename, "r", newline="") as f:
    csvreader = csv.reader(f, delimiter=",")

    print(csvreader)  # <_csv.reader object at 0x000001C9ACC0C3A0> iterator
    read_fields = next(csvreader)  # odczyta jeden element, ustawi odczyt na nastęny

    for row in csvreader:
        read_rows.append(row)

print("Fields:", read_fields)  # Fields: ['name', 'branch', 'year', 'coe']
print("Rows:", read_rows)  # Rows: [['Radek', 'coe', '3', '90']]
print(read_rows[0][0])  # Radek, pierwszy wiersz, pierwszy element
