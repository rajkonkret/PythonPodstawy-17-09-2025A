# krotka, tupla - do odczytu, niemutowalna kolekcja
# pozwala efektywniej zarządzać pamięcią
# stałą - zmienna niezmienna

tupla_imiona = ("Radek", "Tomek", "Zenek", "Roman")
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Roman')
print(type(tupla_imiona))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

tupla = 43,
print(type(tupla))
print(tupla)
# <class 'tuple'>
# (43,)

# PEP8 zaleca by tuple jednoelementową tworzyc z nawiasami ()
tupla2 = ("Radek",)
print(type(tupla2))
print(tupla2)
# <class 'tuple'>
# ('Radek',)

# tupla_liczby[3] = 123  # TypeError: 'tuple' object does not support item assignment

del tupla_liczby  # skasowanie calej tupli
# print(tupla_liczby) # NameError: name 'tupla_liczby' is not defined, zostałą skasowana

print(tupla_imiona.index("Radek"))  # indeks 0
print(tupla_imiona.count("Radek"))  # występuje 1 raz
