# funkcja lambda
# skrócony zapis funkcji
# return

def odejmij(a, b):
    return a - b


print(odejmij(6, 8))  # -2

# lambda zawsze ma return
odejmij2 = lambda a, b: a - b
print(odejmij2(5, 8))  # -3

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(10))  # nastolatek
print(wiek(18))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 35, 55, 60, 100, 500]
l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]

# funkcja wyższego rzędu - przyjmuje inną funkcję jako argument
# map()
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 70, 110, 120, 200, 1000]

# jako funkcja anonimowa
# uzycie funkcji w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 70, 110, 120, 200, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
# Zastosowanie map(): [4, 8, 12, 16, 140, 220, 240, 400, 2000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 5, lista))}")
# Zastosowanie map(): [5, 10, 15, 20, 175, 275, 300, 500, 2500]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 5:
        l3.append(i)
print(l3)  # [1, 2, 3, 4]

# filter()
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 5, lista))}")
# Zastosowanie filter(): [1, 2, 3, 4]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 5 and x < 200, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 5 < x < 200, lista))}")
# Zastosowanie filter(): [35, 55, 60, 100]
# Zastosowanie filter(): [35, 55, 60, 100]
