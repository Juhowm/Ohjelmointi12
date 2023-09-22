import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='3042',
         autocommit=True
         )


def get_airports_by_country_code(country_code):
    cursor = yhteys.cursor()
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country = '{country_code}' GROUP BY type"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return result
    else:
        return "Ei löydy"

kentät = get_airports_by_country_code(input("Syötä maakoodi: "))
print(f"Lentokenttiä on {kentät}")
