from geopy.distance import geodesic as GD
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='3042',
         autocommit=True
         )


def get_location_by_icao_code(icao_code):
    cursor = yhteys.cursor()
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_code}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return result
    else:
        exit("Kirjoita oikea ICAO")

sijainti1 = get_location_by_icao_code(input("Syötä ICAO-koodi: "))
sijainti2 = get_location_by_icao_code(input("Syötä toisen kentän ICAO-koodi: "))
print(f"Näiden kenttien välinen etäisyys on {GD (sijainti1,sijainti2).km}km")
