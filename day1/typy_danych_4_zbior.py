# zbiór (set) - przechowują unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie ma indexu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# pusty zbior
zb2 = set()  # tworzenie pustego zbioru tylko i wyłącznie słówkiem set()
print(zb2)  # set() - pusty zbior
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(24)
zbior.add(32)
zbior.add(17)
print(zbior)
# {32, 33, 66, 777, 11, 44, 17, 18, 22, 55, 24}

# usuniecie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {32, 33, 66, 777, 11, 44, 17, 18, 22, 24}

# pop() - usunięcie pierwszego elementu
print(zbior.pop())  # 32
print(zbior)  # {33, 66, 777, 11, 44, 17, 18, 22, 24}

print(zbior.pop())  # 33
# zbior.pop().pr i tabulator

zmienna = zbior.pop()
print("usunięty:", zmienna)  # usunięty: 66

# operacje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62}

# częśc wspólna - zwraca nowy zbiór
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różica - zwraca nowy zbiór
print(zbior - zbior_2)  # {24, 777, 17, 22}
print(zbior.difference(zbior_2))  # {24, 777, 17, 22}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# update() - do zbioru dopisuje elementy drugiego zbioru
# zmienia bazowy !!!
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62} zmienił sie zbior!!!

krotka = tuple(zbior)
print(krotka)  # (777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62)

# sprawdzenie czy eleemnt istnieje w...
print(777 in zbior)  # True#           True
print(777 in lista)  # True#           True
print(777 in krotka)  # True#          True
print(767 in zbior)  # False#          False
