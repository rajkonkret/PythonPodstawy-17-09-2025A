# while - sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat1")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break

print(licznik)  # 11
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
