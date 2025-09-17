# PEP8 - zasady czystego kodu w pythonie, https://peps.python.org/pep-0008/
import sys

print()  # wypisz/wydrukuj
# Process finished with exit code 0 - program zakończył sie poprawnie, bez błędu
print("Radek")  # Radek
print('Radek')  # Radek

# ctrl / - szybkie wstawienie komentarza
# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-17-09-2025\day1\pierwszy.py", line 8
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 8) - program zakońćzył się z błędem

print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
print("Nazywam się Radek!!!")  # Nazywam się Radek!!!
# ctrl d - powielanie linii

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, dane tekstowe, string

print("39")  # 39
print("39" + "39")  # 3939, łączy teksty, konkatenacja

print("39" "39")  # 3939

print(39)  # 39
print(type(39))  # <class 'int'>, integer, liczba całkowita
print(39 + 39)  # 78
# ctrl alt l - formatowanie zgodne z PEP8

# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie - zamiana na inny typ
print(int("39") + 39)  # 78, int() - rzutowanie na int

print("39" + str(39))  # str() - rzutowanie na tekst, 3939

print(168 * 35)  # 5880
print("168" * 35)
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168

print(50 * "-")
# --------------------------------------------------

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300,
# str_digits_check_threshold=640)

# zmienna - pudełko na dane, posiada nazwę
# snake_case
# nazwa zmiennej powinna podpowiadać co zawiera

# typowanie dynamiczne
# przyjmuje typ na podstawie danych jakie zawiera
name = "Radek"
print(name)  # wypisało zawartość zmiennej
print(type(name))  # <class 'str'>

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

# podpowiedzi typów
name: str = "Radek"
print(type(name))  # <class 'str'>

name = 90  # podkreśla na zółto, uważaj co robisz
print(name)  # 90
