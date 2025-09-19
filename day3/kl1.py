# programownie obiektowe
# klasa - szablon, przepis, opis
# obiekt - instancja klasy - stworzony wg przepisu
# klasa musi byc zadeklarowana przed uzyciem
# tworzenie obiektu wywołuje metode inicjalizującą (konstruktor)
# paradygmaty programowania obiektowego
# hermetezycja, dziedziczenie, polimorfizm, abstrakcja

# PEP8 zaleca by robić PasaclCase UpperCamelCase
class Human:
    """
    Klasa Human w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"


cz1 = Human()
print(cz1.__doc__)  # Klasa Human w Pythonie, dokumentacja
# pydoc  - serwer dokumentacji
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz1.imie = "Radek"
cz1.wiek = 45
cz1.plec = "m"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 45
# m

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 25
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Anna
# 25
# k
