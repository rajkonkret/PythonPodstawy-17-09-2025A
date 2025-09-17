tekst = "Witaj"

print(tekst)
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ
upper_case = tekst.upper()
print(upper_case)  # WITAJ
print(tekst)  # Witaj

tekst = "Witaj Świecie"

print(tekst.capitalize())  # Witaj świecie
print(tekst.lower())  # witaj świecie

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunie wiodące i końcowe białe znaki i spacje
print(tekst.removeprefix("Witaj").strip())  # "Świecie"

encoded_s = tekst.encode("utf-8")
print(encoded_s)  # b'Witaj \xc5\x9awiecie'
print(type(encoded_s))  # <class 'bytes'> dane bajtowe
# \xc5\x9a unicode dla literki Ś w systemie szesnastkowym
print(encoded_s.decode("utf-8"))  # Witaj Świecie

print(tekst)
# Witaj Świecie
# 0123456789... - indeksujemy od 0

print(tekst[4])  # j, litera o indeksie 4, czyli na piątym miejscu

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # wystepuje 0 razy, indeksy 0123
print(tekst.count("j", 0, 4))

imie = "Radek"
print(imie)  # Radek
print("Imie:", imie)  # Imie: Radek

starszy = "Witaj %s!"  # %s - str, wstawi wartość zmiennej
print(starszy % imie)  # Witaj Radek!

# f - string
tekst_format = f"Mama na imię {imie} i lubie pythona."
print(tekst_format)  # Mama na imię Radek i lubie pythona.

tekst_format = f"\tMam na imię {imie}\n i lubie pythona.\b"
print(tekst_format)
# "	 Mam na imię Radek
#  i lubie pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

print("Witaj {} {}".format(imie, "Tomek"))  # Witaj Radek Tomek

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

# komentarz dokumentacyjny
"""Komentarz
    wielolinijkowy"""
