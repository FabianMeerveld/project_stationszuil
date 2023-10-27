import requests
import psycopg2

key = "b843235546375e04da44b6fb8b10f175"


def GetWeather(plaats, land):  #plaatsnaam en landcode
    link = f"http://api.openweathermap.org/geo/1.0/direct?q={plaats},{land}&limit=1&appid={key}"
    response = requests.get(link)
    data = response.json()[0]
    lat = data["lat"]
    lon = data["lon"]
    link = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}"
    response = requests.get(link)
    weather = response.json()["list"]
    info = []
    for i in weather:
        b = i["dt_txt"]
        if "12" in b or i == weather[0]:
            temp = int(i["main"]["temp"] - 273)
            date = b.split(" ")[0].split("-")
            date = date[1], date[2]
            weather_image_id = i["weather"][0]["icon"]
            info_temp = (date, weather_image_id, temp)
            info.append(info_temp)

    return info

def Make_connenction():
    host = '20.160.193.51'
    port = 5432
    name = 'stationszuil'
    user = 'postgres'
    password = 'Bami'
    info_string = f"host='{host}' port='{port}' dbname='{name}' user='{user}' password='{password}'"
    connection = psycopg2.connect(info_string)
    return connection

def Get_review(station):
    connection = Make_connenction()
    cursor = connection.cursor()
    query = f"""SELECT bericht, naam
                FROM review
                WHERE station = '{station}'
                ORDER BY datum_ingedient DESC
                LIMIT 5
                """
    cursor.execute(query)
    records = cursor.fetchall()
    return records

def Get_stationinfo(station):
    connection = Make_connenction()
    cursor = connection.cursor()
    query = f"""SELECT *
                FROM station_service
                WHERE station_city = '{station}'
                """
    cursor.execute(query)
    records = cursor.fetchall()
    return records[0]

station = "Amsterdam"
reviews = Get_review(station)
stationinfo = Get_stationinfo(station)
weer = GetWeather(station,stationinfo[1])

print(reviews)
print(stationinfo)
print(weer)




