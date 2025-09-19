# plik csv - dane oddzielone znakiem podziału ,;tab
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

fields = ['name', 'branch', 'year', 'coe']
row = ["Radek", "coe", "3", 90]

filename = 'records.csv'

# newline="" - ominięcie problemu pustych wierszy
with open(filename, "w", newline="") as fh:
    csvwriter = csv.writer(fh)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)
