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