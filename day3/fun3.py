# stworzyc funkcję obliczającą średnią (ocen)

def liczby(name=None, *cyfry):  # * dowolną ilośc danych pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma_p = sum(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi: {avg}")
        print(f"Średnia dla ucznia {name} wynosi: {avg_p}")
    finally:
        print("Kolejny uczen")


liczby()  # () pusta krotka
liczby(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
# ()
# Bład: division by zero
# Kolejny uczen
# (1, 2, 3, 4, 5)
# Średnia wynosi: 3.0
# Kolejny uczen
liczby("Radek", 7, 7, 7, 7, 7)


# (7, 7, 7, 7, 7)
# Średnia dla ucznia Radek wynosi: 7.0
# Kolejny uczen

def connect(**opcje):  # dowolna ilość argumentów nazwanych
    print(opcje)


connect()
connect(a=7)
# {} 3 słownik
# {'a': 7}
connect(name="Radek")  # {'name': 'Radek'}


def all_args(*args, **kwargs):
    print(f"{args=}")
    print(f"{kwargs=}")


all_args(1, 2, 3)
all_args(a=1, b=2, c=3)
# args=(1, 2, 3)
# kwargs={}
# args=()
# kwargs={'a': 1, 'b': 2, 'c': 3}
all_args(1, 2, name="radek")
# args=(1, 2)
# kwargs={'name': 'radek'}
