a = 10
b = 10


def dodaj():
    a = 7  # zmiienne lokalne, nie zmienia wartości zmiennej globalnej
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # uzyje globalnych


def dodaj3():
    global a  # użyj zmiennej globalnej a
    a = 9  # zmieni wartość zmiennej globalnej a
    b = 90
    print(a + b)


print(f"Wartość a z góry: {a}")  # Wartość a z góry: 10
dodaj()  # 15
print(f"Wartość a z góry: {a}")  # Wartość a z góry: 10
dodaj2()  # 20 uzyje globalnych
print(f"Wartość a z góry: {a}")  # Wartość a z góry: 10
dodaj3()  # 99
print(f"Wartość a z góry: {a}")  # Wartość a z góry: 9
dodaj2()  # a=9, b=10, 19
