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

tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2
print(a, b)  # 1 2

# rozpakowanie tupli
a, b = tup
print(a, b)  # 1 2

tup2 = 1, 2, 3
# a, b = tup2  # ValueError: too many values to unpack (expected 2)
a, *b = tup2  # * worek na dane (kolekcja)
print(a, b)  # 1 [2, 3]

print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Roman')
# name1, name2, name3

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Roman']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek'] Roman

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Tomek'] Zenek Roman

print(sorted(tupla_imiona))  # ['Radek', 'Roman', 'Tomek', 'Zenek'], zwrócił listę
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Roman'), krotka się nie zmieni, jest niemutowalna

lista_z_tupli = list(tupla_imiona)
print(lista_z_tupli)  # ['Radek', 'Tomek', 'Zenek', 'Roman']
print(type(lista_z_tupli))  # <class 'list'>
