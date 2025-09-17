# kolekcje

# lista - przechowuje dowolną ilość danych, dowolnego typu na raz
# zachowuje kolejnośc przy dodawaniu elementów

# tworzenie pustej listy
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Zenek")
lista.append("Aga")
print(lista)  # ['Radek', 'Tomek', 'Marek', 'Zenek', 'Aga']
# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Aga']
#     0        1        2         3       4
#     -5       -4       -3       -2       -1
print(lista[1])  # Tomek
print(lista[3])  # Zenek

# ctrl /
# print(lista[10])  # IndexError: list index out of range

print(len(lista))  # wypisze liczbę elementów w liście, 5
print(lista[4])  # Aga
print(lista[len(lista) - 1])
print(lista[-1])  # Aga - ostatni element z listy
print(lista[-2])  # Zenek

# fragment listy - slicowanie
print(lista[0:3])  # ['Radek', 'Tomek', 'Marek'] 012
print(lista[:3])  # ['Radek', 'Tomek', 'Marek'] 012
print(lista[2:])  # ['Marek', 'Zenek', 'Aga'] - włącznie z ostatnim
print(lista[2:4])  # ['Marek', 'Zenek'], bez ostatniego

print(lista[2:15])  # ['Marek', 'Zenek', 'Aga']
print(lista[20:234])  # []

print(lista[:])  # ['Radek', 'Tomek', 'Marek', 'Zenek', 'Aga']
print(lista[2:2])  # []

print(lista[2:3])  # ['Marek']

print(lista[::2])  # [start:stop:krok], ['Radek', 'Marek', 'Aga'] co drugi

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Aga']
#     0        1        2         3       4
#     -5       -4       -3       -2       -1
print(lista[-2:0])  # [], [3:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Marek'], 0:3

# generowanie listy
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14]

# w odwrotnej kolejności
print(lista_15[::-1])  # [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lista_15[::-3])  # [14, 11, 8, 5, 2]

# nadpisanie elementu
lista[3] = "Radek"
print(lista)  # ['Radek', 'Tomek', 'Marek', 'Radek', 'Aga']

# dopisanie elemntu do listy we wskazanym miejscu (indeksie)
lista.insert(1, "Roman")
print(lista)
# ['Radek', 'Roman', 'Tomek', 'Marek', 'Radek', 'Aga']

# sprawdzenie indexu dla danego elementu, zwraca pierwsze wystąpienie
print(lista.index("Radek"))  # 0

print(lista.count("Radek"))  # 2, występuje 2 razy

# usunięcie lementu, pierwszy napotkany
lista.remove("Radek")
print(lista)  # ['Roman', 'Tomek', 'Marek', 'Radek', 'Aga']

# usunięcie po indeksie, zwraca co usunął
print(lista.pop(4))  # Aga
print(lista)  # ['Roman', 'Tomek', 'Marek', 'Radek']
print(lista.pop())  # usunie ostatni, Radek

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista2 = lista  # kopia referencji, kopia adresu
lista_copy = lista.copy()  # kopiowanie elementów listy do innej listy
print(lista)  # ['Roman', 'Tomek', 'Marek']
print(lista2)  # ['Roman', 'Tomek', 'Marek']
lista.clear()  # usunięcie wszystkich elementów z listy
print(lista)  # []
print(lista2)  # []
print(lista_copy)  # ['Roman', 'Tomek', 'Marek']
print(id(lista))  # 2157460169728
print(id(lista2))  # 2157460169728
print(id(lista_copy))  # 2970338756736

liczby = [54, 999, 34, 22, 12.34, 567]
print(liczby)  # [54, 999, 34, 22, 12.34, 567]
print(type(liczby))  # <class 'list'>

liczby.sort()  # zmiana oryginału
print(liczby)  # [12.34, 22, 34, 54, 567, 999]
liczby.sort(reverse=True)
print(liczby)  # [999, 567, 54, 34, 22, 12.34]

liczby = [54, 999, 34, 22, 12.34, 567, "A"]
print(liczby)  # [54, 999, 34, 22, 12.34, 567, 'A']
print(type(liczby))  # <class 'list'>
# liczby.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

lista_copy.reverse()  # tylko odwrócenie
print(lista_copy)  # ['Marek', 'Tomek', 'Roman']

# rozpakowanie sekwencji
tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista1)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('P', 'y', 't', 'h', ' ', 'o', 'n', '.')
