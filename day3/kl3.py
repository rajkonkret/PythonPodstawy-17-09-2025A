from abc import ABC, abstractmethod


# klasa abstrakcja
# metode abstrakcyjną
class Ptak(ABC):
    """
    Kalsa Ptak
    """

    def __init__(self, gatunek, szybkosc):
        """

        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print('Tu', self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Dziedziczy z klasy Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # obowiązkowo, konstruktor z klasy wyzszej

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("ko ko ko ko ko")


class Orzel(Ptak):
    """
    Dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("Kier kir kier")


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# print(or1.gatunek)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# print(kur1.gatunek)
# kur1.latam()  # Tu Kura Lecę z szybkością 0
#
kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()  # ko ko ko ko ko
or2 = Orzel("Orzel", 67)
or2.latam()
or2.wydaj_odglos()
# Tu Orzel Lecę z szybkością 67
# Kier kir kier

# polimorfizm
lista = [or2, kur2]
for i in lista:
    i.wydaj_odglos()
    # Kier kir kier
    # ko ko ko ko ko
