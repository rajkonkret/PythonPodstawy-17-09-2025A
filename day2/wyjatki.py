#  wyjątek - bład podczas wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-17-09-2025\day2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("a" * "23")
    # print(int("a"))
    # raise KeyError("Brak klucza")
    value = 90 / 3
except ZeroDivisionError:
    print('Nie dziel przez zero')
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Błąd:", e)
else:  # gdy nie ma błedu
    print(value)
finally:  # wypisze się zawsze
    print('Kolejne dane')
print('Dalsza cześć programu')
# Nie dziel przez zero
# Dalsza cześć programu
# Błąd typu
# Dalsza cześć programu
# Błąd: 'Brak klucza'
# Dalsza cześć programu
# 30.0
# Dalsza cześć programu
