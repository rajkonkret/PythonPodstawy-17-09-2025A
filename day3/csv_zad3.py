import pandas

# pip install pandas
# C:\\Users\\CSComarch\\PycharmProjects\\PythonPodstawy-17-09-2025\\day3\\csv_zad3.py
data = pandas.read_csv('records.csv', delimiter=",")
print(data)
#     name branch  year  coe
# 0  Radek    coe     3   90
# 1  Radek    coe     3   90
# 2  Radek    coe     3   90
# 3  Radek    coe     3   90
# 4  Radek    coe     3   90
# 5  Radek    coe     3   90

print(data.columns)
# Index(['name', 'branch', 'year', 'coe'], dtype='object')
print(data.values)
# [['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]]

print(data.items())
# Index(['name', 'branch', 'year', 'coe'], dtype='object')
# [['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]
#  ['Radek' 'coe' 3 90]]
# <generator object DataFrame.items at 0x0000028244504310>
