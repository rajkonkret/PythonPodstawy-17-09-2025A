import random

# operacja na liczbach pseudolosowych

"""Return random integer in range [a, b], including both end points.
        """
print(random.randint(1, 100))  # int od 1 do 100

print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int, od 0 do 4

print(random.random())  # float, 0.8573204147784357, od 0 do 0.99999999
print(random.random() * 9)  # float, 7.5787383915177, od 0 do 8.99999999

lista = [67, 45, 32, 68, 69, 90, 42]
print(random.randrange(len(lista)))
print(random.choice(lista))  # jeden element z listy, 32

lista_kula = list(range(1, 50))  # od 1 do 49
# print(lista_kula)

wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)

print(random.choices(lista_kula, k=6))  # [9, 41, 41, 30, 20, 31], z powtórzeniami
print(random.sample(lista_kula, k=6))  # [5, 33, 10, 7, 44, 26]
print(random.sample(lista_kula, 6))  # [5, 33, 10, 7, 44, 26]
# [19, 41, 8, 47, 49, 24]
# [36, 14, 39, 49, 18, 25]
