# baza danych - system przechowywania danych

# sql, nosql
import sqlite3

# sqlite - baza daanych w jedym pliku, lub w pamięci

sql_connection = None

try:
    sql_connection = sqlite3.connect("baza.db")
    cursor = sql_connection.cursor()
    print('Baza danych zostałą podłaczona')

    query = """CREATE TABLE IF NOT EXISTS developers
               (
                   id
                   INTEGER
                   PRIMARY
                   KEY
                   NOT
                   NULL,
                   name
                   TEXT
                   NOT
                   NULL,
                   salary
                   REAL
                   NOT
                   NULL
               );"""

    # cursor.execute(query)
    # sql_connection.commit()
    insert = """
             INSERT INTO developers(id, name, salary)
             VALUES (3, 'Tomek', 20000);
             """

    # cursor.execute(insert)
    # sql_connection.commit()
    update = """
             UPDATE developers
             set salary=30000
             WHERE id = 1;
             """

    # cursor.execute(update)
    # sql_connection.commit()

    for row in cursor.execute("SELECT * FROM developers;"):
        print(row)
# (1, 'Radek', 30000.0)
# (2, 'Radek', 20000.0)
# (3, 'Tomek', 20000.0)
except sqlite3.Error as e:
    print("Błąd:", e)
finally:  # wykonuje się zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
