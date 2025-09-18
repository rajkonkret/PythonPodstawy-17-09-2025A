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
