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
