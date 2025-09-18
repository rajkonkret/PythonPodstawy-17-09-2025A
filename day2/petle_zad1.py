# pętla - możliwośc wykonania wielokrotnie tego samego fragmentu kodu
# for - iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(5):
    pass  # nic nie rób

for _ in range(3):  # niema zmienna
    print("Test podłoga")
    # print(_)
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# 2

for i in range(10):
    print(i * 2)
    print(i + 2)

# przerobic zadanie lotto na pętle
lista_kula = list(range(1, 50))  # od 1 do 49
# print(lista_kula)
lista_wynik = []
for _ in range(6):  # od 0 do 5
    wyn = random.choice(lista_kula)
    lista_kula.remove(wyn)
    # print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [20, 8, 5, 7, 30, 2]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:  # dla wszystkich elementów kolekcji lista3
    if c > 4:
        print(c, "Większe od 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, 'Mniejsze od 4')
# 0 Mniejsze od 4
# 2 Mniejsze od 4
# 4 Równe 4
# 6 Większe od 4
# 8 Większe od 4
for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -3):
    print(i)
# 10
# 7
# 4
# 1

for c in lista3:
    if c == 2:
        c += 1
        print(c)  # tylko dla c==2
    print("Za każdym przejściem pętli")

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(imiona)
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek
for i in range(len(imiona)):  # generujemy po kolei indeksy
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - numeruje kolekcje i zwraca numer i element kolekcji
for i in enumerate(imiona):
    print(i)
# (0, 'Radek') krotka
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
i, o = (3, 'Ania')
for i, o in enumerate(imiona):  # rozpakowanie krotki w locie
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):  # rozpakowanie krotki w locie
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

# imiona = ["Radek", "Tomek", "Zenek", "Ania"]
imiona = ["Radek", "Tomek", "Zenek", "Ania", "Aga"]
wiek = [45, 65, 34, 20]

# Radek 45
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
# Radek 45
# Tomek 65
# Zenek 34
# Ania 20
# IndexError: list index out of range, dla różnych długości list

# zip() - łączenie kolekcji
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 45)
# ('Tomek', 65)
# ('Zenek', 34)
# ('Ania', 20)
for o, w in zip(imiona, wiek):
    print(o, w)
# Radek 45
# Tomek 65
# Zenek 34
# Ania 20

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 45))
# (1, ('Tomek', 65))
# (2, ('Zenek', 34))
# (3, ('Ania', 20))
(a, (b, c)) = (3, ('Ania', 20))
print(a, b, c)  # 3 Ania 20
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 45
# 1 Tomek 65
# 2 Zenek 34
# 3 Ania 20
