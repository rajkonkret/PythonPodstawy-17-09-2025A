user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe
liczba = 890123654789  # int

print("Witaj %s, masz teraz %d lat" % (user, wiek))
# %d - digit
# %s - string

# sprawdzaja typ danych
# TypeError: %d format: a real number is required, not str
# print("Witaj %d, masz teraz %s lat" % (user, wiek))

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - string - sformmatowany tekst

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
# %f - float
print("Używamy wersji pythona %.2f" % 3)  # Używamy wersji pythona 3.00
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4- zaokrągla
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4- zaokrągla

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.90001
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4

user = "Tomek"
print(f"{user:>10}")  # "     Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 890123654789
print(f'Nasza duża liczba: {liczba:,}')  # Nasza duża liczba: 890,123,654,789
print(f'Nasza duża liczba: {liczba:_}')  # Nasza duża liczba: 890_123_654_789
print(f'Nasza duża liczba: {liczba:_}'.replace("_", " "))  # Nasza duża liczba: 890 123 654 789
print(f'Nasza duża liczba: {liczba:_}'.replace("_", ","))  # Nasza duża liczba: 890,123,654,789

# liczba2 = 1500000000000
liczba2 = 1_500_000_000_000
print(liczba2)
print(type(liczba2))  # <class 'int'>
