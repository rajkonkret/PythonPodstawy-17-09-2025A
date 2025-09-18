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

# password = input("Podaj hasło")
# while password != "secret":  # !=  - różne od
#     password = input("Błędne hasło. Podaj ponownie")
# print("Hasło prawidłowe")
# Podaj hasłoddd
# Błędne hasło. Podaj ponownieasdasdsa
# Błędne hasło. Podaj ponownieasddasdas
# Błędne hasło. Podaj ponowniesaDADA
# Błędne hasło. Podaj ponownie123
# Błędne hasło. Podaj ponownieSECRET
# Błędne hasło. Podaj ponowniesecret
# Hasło prawidłowe

# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę")
#     #  A string is numeric if all characters in the string are numeric
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
# print(lista)  # ['1', '2', '3', '4', '5', '6']
# print(lista_int)  # [1, 2, 3, 4, 5, 6]
