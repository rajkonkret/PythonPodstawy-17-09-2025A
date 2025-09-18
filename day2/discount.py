from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2025-09-18
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-09-18 15:01:49.946133
print(type(time))  # <class 'datetime.datetime'>

print(time.year)  # 2025
print(time.day)  # 18

# TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# tomorrow = today + 1

#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2025-09-19

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data:", formated_date)  # Sformatowana data: 18/09/2025
print(type(formated_date))  # <class 'str'>

# 15:03
# 3:03 pm
formated_time = datetime.now().strftime("%H:%M:%S")
print(formated_time)  # 15:15:04

formated_time_usa = datetime.now().strftime("%I:%M %p")
print(formated_time_usa)  # 03:16 PM

object_time = datetime.now().strptime("18/09/2025", "%d/%m/%Y")
print(object_time)  # 2025-09-18 00:00:00
print(type(object_time))  # <class 'datetime.datetime'>

print(35 * "-")

products = [
    {"sku": 1, "exp_date": today, "price": 200},
    {"sku": 2, "exp_date": today, "price": 100},
    {"sku": 3, "exp_date": tomorrow, "price": 500},
    {"sku": 4, "exp_date": today, "price": 80},
    {"sku": 5, "exp_date": today, "price": 99.99},
]

for p in products:
    # print(p)  # {'sku': 5, 'exp_date': datetime.date(2025, 9, 18), 'price': 99.99}
    # print(p['exp_date'])  # 2025-09-18
    # if p['exp_date'] == today:
    #     p['price'] *= 0.8
    if p['exp_date'] != today:
        continue
    p['price'] *= 0.8
    print("Zmiana ceny")
    print(f"""
Price for {p['sku']}
is now {p['price']:.2f}""")
# -----------------------------------
# Zmiana ceny
#
# Price for 1
# is now 160.00
# Zmiana ceny
#
# Price for 2
# is now 80.00
# Zmiana ceny
#
# Price for 4
# is now 64.00
# Zmiana ceny
#
# Price for 5
# is now 79.99

"""fgfg
gfgffhfgh"""
'''
dsfsdfsdfsd'''
