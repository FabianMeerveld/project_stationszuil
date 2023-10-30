import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
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
    return records






def MakeGui():
    juiststation = False
    station = ""
    station = simpledialog.askstring(title="Kies station", prompt="Station: ")
    while juiststation == False:
        stationinfo = Get_stationinfo(station)
        if len(stationinfo) >= 1:
            juiststation = True
            stationinfo = stationinfo[0]
        else:
            station = simpledialog.askstring(title="Kies station", prompt="Ongeldig station | Station: ")
    print(stationinfo)
    reviews = Get_review(station)
    weer = GetWeather(station, stationinfo[1])


    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title('Stationszuil')
    root.geometry("800x600")
    root.config(bg="#FFC917")

    root.columnconfigure(0, weight=52)
    root.columnconfigure(1, weight=6)
    root.columnconfigure(2, weight=6)
    root.columnconfigure(3, weight=6)
    root.columnconfigure(4, weight=6)
    root.columnconfigure(5, weight=8)
    root.columnconfigure(6, weight=8)
    root.columnconfigure(7, weight=12)
    root.rowconfigure(0, weight=2)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(2, weight=2)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=2)
    root.rowconfigure(5, weight=2)
    root.rowconfigure(6, weight=2)
    root.rowconfigure(7, weight=2)
    root.rowconfigure(8, weight=2)
    root.rowconfigure(9, weight=2)
    root.rowconfigure(10, weight=2)
    root.rowconfigure(11, weight=2)
    root.rowconfigure(12, weight=2)
    root.rowconfigure(13, weight=2)

    # images
    images = {}
    image = Image.open('images/01d.png')
    img_01d = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_01d"] = img_01d
    image = Image.open('images/02d.png')
    img_02d = ImageTk.PhotoImage(image.resize((100, 100)))
    image = Image.open('images/03d.png')
    img_03d = ImageTk.PhotoImage(image.resize((100, 100)))
    image = Image.open('images/04d.png')
    img_04d = ImageTk.PhotoImage(image.resize((100, 100)))
    image = Image.open('images/09d.png')
    img_09d = ImageTk.PhotoImage(image.resize((100, 100)))

    print(images)
    # tussenlijntjes
    xlineframe = tk.Frame(root, background="#003082")
    xlineframe.grid(column=4, row=0, rowspan=15, sticky="nsew")
    ylineframe = tk.Frame(root, background="#003082")
    ylineframe.grid(column=0, row=3, columnspan=8, sticky="nsew")

    # stationinfo
    stationlabel = tk.Label(root, bg="#FFC917", fg="#003082",text=f" {station}", font="Arial, 45")
    stationlabel.grid(column=0, row=0, rowspan=3, sticky="w")
    stationicon2label = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    stationicon2label.grid(row=0, column=2, sticky="e")
    stationicon3label = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    stationicon3label.grid(row=0, column=3, sticky="w")
    stationicon5label = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    stationicon5label.grid(row=2, column=2, sticky="e")
    stationicon6label = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    stationicon6label.grid(row=2, column=3, sticky="w")

    # tijd
    timelabel = tk.Label(root, bg="#FFC917", fg="#003082",text="12:00:00", font="Arial, 32")
    timelabel.grid(column=5, row=0, columnspan=3, rowspan=3, sticky="nsew")

    # weer
    weer1datumlabel = tk.Label(root, bg="#FFC917", fg="#003082",text="00-00", font="Arial, 50")
    weer1imagelabel = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    weer1templabel = tk.Label(root, bg="#FFC917", fg="#003082",text="0°C", font="Arial, 50")
    weer1datumlabel.grid(column=5, row=4, sticky="nsew", rowspan=2)
    weer1imagelabel.grid(column=6, row=4, sticky="nsew", rowspan=2)
    weer1templabel.grid(column=7, row=4, sticky="nsew", rowspan=2)

    weer2datumlabel = tk.Label(root, bg="#FFC917", fg="#003082",text="00-00", font="Arial, 50")
    weer2imagelabel = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    weer2templabel = tk.Label(root, bg="#FFC917", fg="#003082",text="0°C", font="Arial, 50")
    weer2datumlabel.grid(column=5, row=6, sticky="nsew", rowspan=2)
    weer2imagelabel.grid(column=6, row=6, sticky="nsew", rowspan=2)
    weer2templabel.grid(column=7, row=6, sticky="nsew", rowspan=2)

    weer3datumlabel = tk.Label(root, bg="#FFC917", fg="#003082",text="00-00", font="Arial, 50")
    weer3imagelabel = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    weer3templabel = tk.Label(root, bg="#FFC917", fg="#003082",text="0°C", font="Arial, 50")
    weer3datumlabel.grid(column=5, row=8, sticky="nsew", rowspan=2)
    weer3imagelabel.grid(column=6, row=8, sticky="nsew", rowspan=2)
    weer3templabel.grid(column=7, row=8, sticky="nsew", rowspan=2)

    weer4datumlabel = tk.Label(root, bg="#FFC917", fg="#003082",text="00-00", font="Arial, 50")
    weer4imagelabel = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    weer4templabel = tk.Label(root, bg="#FFC917", fg="#003082",text="0°C", font="Arial, 50")
    weer4datumlabel.grid(column=5, row=10, sticky="nsew", rowspan=2)
    weer4imagelabel.grid(column=6, row=10, sticky="nsew", rowspan=2)
    weer4templabel.grid(column=7, row=10, sticky="nsew", rowspan=2)

    weer5datumlabel = tk.Label(root, bg="#FFC917", fg="#003082",text="00-00", font="Arial, 50")
    weer5imagelabel = tk.Label(root, bg="#FFC917", image=images["img_01d"], fg="#003082",text="")
    weer5templabel = tk.Label(root, bg="#FFC917", fg="#003082",text="0°C", font="Arial, 50")
    weer5datumlabel.grid(column=5, row=12, sticky="nsew", rowspan=2)
    weer5imagelabel.grid(column=6, row=12, sticky="nsew", rowspan=2)
    weer5templabel.grid(column=7, row=12, sticky="nsew", rowspan=2)

    # review
    review1berichtlabel = tk.Label(root, bg="#FFC917",
                                   fg="#070721",text='"Embrace the challenges, for they are the stepping stones to success. Keep learning, growing, and pursuing your dreams"',
                                   font="Arial, 25", wraplength=850)
    review1naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D",text="-{naamplaceholder}", font="Arial 15")
    review1berichtlabel.grid(column=0, row=4, columnspan=2, rowspan=2, sticky="nsew")
    review1naamlabel.grid(column=2, row=5, sticky="nesw")
    review2berichtlabel = tk.Label(root, bg="#FFC917",
                                   fg="#070721",text='"Embrace the challenges, for they are the stepping stones to success. Keep learning, growing, and pursuing your dreams"',
                                   font="Arial, 25", wraplength=850)
    review2naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D",text="-{naamplaceholder}", font="Arial 15")
    review2berichtlabel.grid(column=0, row=6, columnspan=2, rowspan=2, sticky="nsew")
    review2naamlabel.grid(column=2, row=7, sticky="se")
    review3berichtlabel = tk.Label(root, bg="#FFC917",
                                   fg="#070721",text='"Embrace the challenges, for they are the stepping stones to success. Keep learning, growing, and pursuing your dreams"',
                                   font="Arial, 25", wraplength=850)
    review3naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D",text="-{naamplaceholder}", font="Arial 15")
    review3berichtlabel.grid(column=0, row=8, columnspan=2, rowspan=2, sticky="nsew")
    review3naamlabel.grid(column=2, row=9, sticky="se")
    review4berichtlabel = tk.Label(root, bg="#FFC917",
                                   fg="#070721",text='"Embrace the challenges, for they are the stepping stones to success. Keep learning, growing, and pursuing your dreams"',
                                   font="Arial, 25", wraplength=850)
    review4naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D",text="-{naamplaceholder}", font="Arial 15")
    review4berichtlabel.grid(column=0, row=10, columnspan=2, rowspan=2, sticky="nsew")
    review4naamlabel.grid(column=2, row=11, sticky="se")
    review5berichtlabel = tk.Label(root, bg="#FFC917",
                                   fg="#070721",text='"Embrace the challenges, for they are the stepping stones to success. Keep learning, growing, and pursuing your dreams"',
                                   font="Arial, 25", wraplength=850)
    review5naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D",text="-{naamplaceholder}", font="Arial 15")
    review5berichtlabel.grid(column=0, row=12, columnspan=2, rowspan=2, sticky="nsew")
    review5naamlabel.grid(column=2, row=13, sticky="se")


    root.mainloop()


MakeGui()

