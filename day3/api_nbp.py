import requests

#  pip install requests
url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx warningi
# 4xx bład po stronie klienta, 404 - brak strony, 400 Bad Request pomylony parametr
# 5xx - 500 Internal Server Error

print(response.text)
data = response.json()
print(data)
print(type(data))  # <class 'dict'>

# {'table': 'A',
#  'currency': 'dolar amerykański',
#  'code': 'USD',
#  'rates': [{'no': '182/A/NBP/2025', 'effectiveDate': '2025-09-19', 'mid': 3.6278}]}

for i in data:
    print(i)

# table
# currency
# code
# rates

print(data['rates'])
# [
# {'no': '182/A/NBP/2025', 'effectiveDate': '2025-09-19', 'mid': 3.6278}
# ]
print(data['rates'][0])  # {'no': '182/A/NBP/2025', 'effectiveDate': '2025-09-19', 'mid': 3.6278}
print(data['rates'][0]['mid'])  # 3.6278
# https://api.chucknorris.io/
