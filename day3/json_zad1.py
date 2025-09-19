import json

# '{"name":"John", "age":30, "car":null}'
# odpowiednik jsona w pythonie jest słownik

person_dict = {'name': "Radek", "age": 40, "czy_pali": None}
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=True)

# {
#  "name": "Radek",
#  "age": 40,
#  "czy_pali": null
# }

with open("nasze_dane.json", "r") as file:
    data = json.load(file)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>

json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>
