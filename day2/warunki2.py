# od pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.strip().casefold():
    case "python":
        lista.append("Python")
    case "java":
        lista.append("Java")
    case _:  # odpowiednik else
        print("Inny")

print(lista)