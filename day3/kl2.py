class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem w drogę")
        else:
            print('Ruszyłam w drogę')


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Raddek", 45, 189, "m")
print(cz1.imie)  # Raddek
print(cz1.wiek)  # 45
print(cz1.wzrost)  # 189
print(cz1.plec)  # m
cz2 = Human("Anna", 25, 165, "k")
print(cz2.imie)  # Anna
print(cz2.wiek)  # 25
print(cz2.wzrost)  # 165
print(cz2.plec)  # k

cz1.powitanie()
cz2.powitanie()
# Nazywam się Raddek
# Nazywam się Anna

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłem w drogę
# Ruszyłam w drogę
