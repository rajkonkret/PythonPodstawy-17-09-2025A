# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku (True/False) wykona odpowiedni blok programu

# debugger
# pułapki
odp = True
# odp = False
if odp:
    # blok programu, wykona się gdy warunek True
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo

print("Dalsza częśc programu")
# Dalsza częśc programu

odp = "Radek"
print(bool(odp))  # True
if odp:  # czy cokolwiek zawiera
    print("Radek")  # Radek

if odp == "Radek":  # porównanie, czy konkretnie zawiera Radek
    print("Nadal Radek")
# Nadal Radek

odp = 0
if odp:
    print("Działa")
else:  # w przeciwnym przypadku
    print("Zero -> False")
    # Zero -> False

a = "Radek"
if len(a) > 3:
    print(f"Długośc wynosi: {len(a)}, więcej niż 3")
# Długośc wynosi: 5, więcej niż 3

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długośc wynosi: {n}, więcej niż 3")
    #  Długośc wynosi: 5, więcej niż 3

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długośc wynosi: {n}, więcej niż 3")
    # Długośc wynosi: 5, więcej niż 3

# kolejność ma znaczenie
# podatek = 0
# zarobki = int(input("podaj zarobki"))
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:  # wszystko inne
#     podatek = 0.9  # 90%
#
# print(f"Podatek wynosi {podatek * zarobki} pln.")
# # 0.2 dla przedziału od 10000 do 39999

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0
print("Rabat wynosi:", rabat)
# Rabat wynosi: 25

rabat = 25 if sum_zam > 100 else 0  # operator warunkowy
print("Rabat wynosi:", rabat)  # Rabat wynosi: 25

# napisac test z...
punkty = 0
odp = input("Podaj datę Chrztu Polski")
if odp == '966':
    print("Dobrze")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Musisz jescze poczytać")

print("Punkty:", punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
