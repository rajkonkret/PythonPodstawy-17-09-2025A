# słownik - para klucz-wartosc
# {"user" : "Radek"}
# klucze nie mogą się powtarzać
# odpowiednik jsona

# pusty słownik
dictionary = {}
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

pusty_zbior = dict()
print(type(pusty_zbior))  # <class 'dict'>
print(pusty_zbior)  # {}

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 50])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 50)])

dict_list = {'imie': ["Radek", "Tomek", "Zenek"]}
print(dict_list)  # {'imie': ['Radek', 'Tomek', 'Zenek']}

# wypisanie wartości ze słownika
print(dictionary['imie'])  # Radek
print(dict_list['imie'])  # ['Radek', 'Tomek', 'Zenek']
print(dict_list['imie'][1])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get('Imie'))  # None
print(dictionary.get('imie'))  # Radek
print(dictionary.get('Imie', "default"))  # default, zwraca wartość domyślną

dictionary.update({"data": "31-12-2027"})
print(dictionary)  # {'imie': 'Radek', 'wiek': 50, 'data': '31-12-2027'}

# input() - wprowadzanie danych np.:  z klawiatury
# tekst = input("Podaj imię")
# print(tekst)
# Podaj imięRadek
# Radek

# napisac aplikację kalkulator
# pobrac liczby input() x 2
# wyswietlic wynik obliczenia (+) print()
# a = int(input("Podaj pierwszą liczbę:"))
# a = input("Podaj pierwszą liczbę:")  # -> str
# # b = float(input("Podaj drugą liczbę:"))
# b = input("Podaj drugą liczbę:")
# print(f"Wynik {a} + {b} = {int(a) + float(b)}")
# Podaj pierwszą liczbę:4
# Podaj drugą liczbę:5
# Wynik 4 + 5 = 9.0

# # napisać program słownik pol-ang z wykorzstaniem słownika
# pol_ang = {"kot": "cat", "pies": "dog", "dach": "roof"}
# print(f"Znam słowa: {pol_ang.keys()}")
# odp = input("Podaj słówko do przetłumaczenia: ")
# print(f"Tłumaczenie {pol_ang.get(odp.strip().lower(), "Nie ma")}")

name1 = "GROSS"
name2 = "groẞ"

print(name1.lower() == name2.lower())  # False
""" Return a version of the string suitable for caseless comparisons. """
print(name1.casefold() == name2.casefold())  # True
# print(f"Tłumaczenie {pol_ang.get(odp.strip().casefold(), "Nie ma")}")
