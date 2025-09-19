# funkcje - wydzielony fragment kodu, można wywołąć w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# żeby uruchomic funkcję musi zostać wywołana

a = 8
b = 9


# funkcje nie zwracją wyniku
# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z obowiązkowymi argumentami
    print(a + b)


# zasymulowania funkcji z przeciązeniem liczbą argumentów
def odejmij(a, b, c=0):  # argument c ma wartośc domyślną
    print(a - b - c)


# wywołanie funkcji, uruchomienie
# argumenty przekazane po pozycji
dodaj()  # nazwa funkcji i nawiasy (), 17
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(34, 67)  # 101

odejmij(1, 2)  # -1, c=0
odejmij(1, 2, 3)  # -4, c=3

# przekazane po nazwie
odejmij(c=9, a=6, b=98)  # -101
odejmij(b=8, a=10)  # 2

# mieszane
odejmij(1, 2, c=9)  # -10
odejmij(1, b=2, c=9)  # -10

# SyntaxError: positional argument follows keyword argument
# nazwane muszą byc po pozycyjnych
# odejmij(b=2, 1, 2)

# print(dodaj() + dodaj2(6, 90))
print(dodaj())  # None

print(40 * "-")


# funkcje zwracającce wynik
# konczą się słówkiem return
def dodaj3():
    return a + b


def odejmij2(a=7, b=0, c=0):
    return a - b - c


print(dodaj3())  # 17
zm = dodaj3()
print("Wynik:", zm)  # Wynik: 17

print(odejmij2(5, 8, 9))  # -12
print(dodaj3() + odejmij2(4, 5, 6))  # 10
