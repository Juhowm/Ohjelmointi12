import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='3042',
         autocommit=True
         )


def get_country_by_icao_code(icao_code):
    cursor = yhteys.cursor()
    sql = f"SELECT ident, name, municipality FROM airport WHERE gps_code = '{icao_code}'"
    cursor.execute(sql)
    result = cursor.fetchmany()
    if result:
        return result[0]
    else:
        return "Ei löydy"


country = get_country_by_icao_code(input("Syötä icao-koodi: "))
print(f"Lentokentän nimi on {country[1]} ja se sijaitsee kunnassa {country[2]}")
