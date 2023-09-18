import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game2',
         user='root',
         password='3042',
         autocommit=True
         )


def get_country_by_iso_code(iso_code):
    cursor = yhteys.cursor()
    sql = f"SELECT iso_country, name FROM country WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return result[1]
    else:
        return "no results"


country = get_country_by_iso_code('FI')
print(country)
country = get_country_by_iso_code(input("Syötä maakoodi: "))
print(country)


def update_country_by_iso_code(iso_code, country_name):
    cursor = yhteys.cursor()
    sql = f"UPDATE country SET name='{country_name}' WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    if (cursor.rowcount) > 0:
        return f"code '{iso_code} updated to '{country_name}"
    else:
        return f"koodia ei löytynyt"


country_code = input("Anna muokattava koodi: ")
new_name = input("Anna maalle uusi nimi: ")
tulos = update_country_by_iso_code(country_code, new_name)
print(tulos)
