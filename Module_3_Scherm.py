import tkinter as tk
import time
from tkinter import simpledialog
from PIL import Image, ImageTk
import requests
import psycopg2

key = "b843235546375e04da44b6fb8b10f175"


def GetWeather(plaats, land):  # plaatsnaam en landcode
    link = f"http://api.openweathermap.org/geo/1.0/direct?q={plaats},{land}&limit=1&appid={key}"
    response = requests.get(link)
    data = response.json()[0]
    lat = data["lat"]
    lon = data["lon"]
    link = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}"
    response = requests.get(link)
    weather = response.json()["list"]
    info = []
    today = False
    for i in weather:
        b = i["dt_txt"]
        today = False
        if "12" in b:
            if i == weather[0]:
                today = True
            temp = int(i["main"]["temp"] - 273)
            date = b.split(" ")[0].split("-")
            date = date[1], date[2]
            weather_image_id = i["weather"][0]["icon"]
            info_temp = (date, weather_image_id, temp)
            info.append(info_temp)
    if not today:
        i = weather[0]
        b = i["dt_txt"]
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
    stationinfo = None
    juiststation = False
    station = simpledialog.askstring(title="Kies station", prompt="Station: ")
    while not juiststation:
        stationinfo = Get_stationinfo(station)
        if len(stationinfo) >= 1:
            juiststation = True
            stationinfo = stationinfo[0]
        else:
            station = simpledialog.askstring(title="Kies station", prompt="Ongeldig station | Station: ")
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
    images["img_02d"] = img_02d
    image = Image.open('images/03d.png')
    img_03d = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_03d"] = img_03d
    image = Image.open('images/04d.png')
    img_04d = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_04d"] = img_04d
    image = Image.open('images/09d.png')
    img_09d = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_09d"] = img_09d
    image = Image.open('images/10d.png')
    img_10d = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_10d"] = img_10d
    image = Image.open('images/11d.png')
    img_11d = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_11d"] = img_11d
    image = Image.open('images/13d.png')
    img_13d = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_13d"] = img_13d
    image = Image.open('images/50d.png')
    img_50d = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_50d"] = img_50d
    image = Image.open('images/img_pr.png')
    img_pr = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_pr"] = img_pr
    image = Image.open('images/img_ovfiets.png')
    img_ovfiets = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_ovfiets"] = img_ovfiets
    image = Image.open('images/img_lift.png')
    img_lift = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_lift"] = img_lift
    image = Image.open('images/img_toilet.png')
    img_toilet = ImageTk.PhotoImage(image.resize((100, 100)))
    images["img_toilet"] = img_toilet
    img1 = None
    img2 = None
    img3 = None
    img4 = None
    if stationinfo[2]:
        img1 = images["img_ovfiets"]
        if stationinfo[3]:
            img2 = images["img_lift"]
            if stationinfo[4]:
                img3 = images["img_toilet"]
                if stationinfo[5]:
                    img4 = images["img_pr"]
            elif stationinfo[5]:
                img3 = images["img_pr"]
        elif stationinfo[4]:
            img2 = images["img_toilet"]
            if stationinfo[5]:
                img3 = images["img_pr"]
        elif stationinfo[5]:
            img2 = images["img_pr"]
    elif stationinfo[3]:
        img1 = images["img_lift"]
        if stationinfo[4]:
            img2 = images["img_toilet"]
            if stationinfo[5]:
                img3 = images["img_pr"]
        elif stationinfo[5]:
            img2 = images["img_pr"]
    elif stationinfo[4]:
        img1 = images["img_toilet"]
        if stationinfo[5]:
            img2 = images["img_pr"]
    elif stationinfo[5]:
        img1 = images["img_pr"]
    # tussenlijntjes
    xlineframe = tk.Frame(root, background="#003082")
    xlineframe.grid(column=4, row=0, rowspan=15, sticky="nsew")
    ylineframe = tk.Frame(root, background="#003082")
    ylineframe.grid(column=0, row=3, columnspan=8, sticky="nsew")

    # stationinfo
    stationlabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f" {station}", font="Arial, 45")
    stationlabel.grid(column=0, row=0, rowspan=3, sticky="w")
    stationicon2label = tk.Label(root, bg="#FFC917", image=img1, fg="#003082", text="")
    stationicon2label.grid(row=0, column=2, sticky="e")
    stationicon3label = tk.Label(root, bg="#FFC917", image=img3, fg="#003082", text="")
    stationicon3label.grid(row=0, column=3, sticky="w")
    stationicon5label = tk.Label(root, bg="#FFC917", image=img2, fg="#003082", text="")
    stationicon5label.grid(row=2, column=2, sticky="e")
    stationicon6label = tk.Label(root, bg="#FFC917", image=img4, fg="#003082", text="")
    stationicon6label.grid(row=2, column=3, sticky="w")

    # tijd
    def tijd():
        nutijd = time.strftime("%H:%M:%S")
        timelabel.config(text=nutijd)
        timelabel.after(1000, tijd)

    timelabel = tk.Label(root, bg="#FFC917", fg="#003082", text="12:00:00", font="Arial, 45")
    timelabel.grid(column=5, row=0, columnspan=3, rowspan=3, sticky="nsew")

    # weer
    weer1datumlabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[0][0][0]}-{weer[0][0][1]}",
                               font="Arial, 50")
    weer1imagelabel = tk.Label(root, bg="#FFC917", image=images[f"img_{weer[0][1]}"], fg="#003082", text="")
    weer1templabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[0][2]}°C", font="Arial, 50")
    weer1datumlabel.grid(column=5, row=4, sticky="nsew", rowspan=2)
    weer1imagelabel.grid(column=6, row=4, sticky="nsew", rowspan=2)
    weer1templabel.grid(column=7, row=4, sticky="nsew", rowspan=2)

    weer2datumlabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[1][0][0]}-{weer[1][0][1]}",
                               font="Arial, 50")
    weer2imagelabel = tk.Label(root, bg="#FFC917", image=images[f"img_{weer[1][1]}"], fg="#003082", text="")
    weer2templabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[1][2]}°C", font="Arial, 50")
    weer2datumlabel.grid(column=5, row=6, sticky="nsew", rowspan=2)
    weer2imagelabel.grid(column=6, row=6, sticky="nsew", rowspan=2)
    weer2templabel.grid(column=7, row=6, sticky="nsew", rowspan=2)

    weer3datumlabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[2][0][0]}-{weer[2][0][1]}",
                               font="Arial, 50")
    weer3imagelabel = tk.Label(root, bg="#FFC917", image=images[f"img_{weer[2][1]}"], fg="#003082", text="")
    weer3templabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[2][2]}°C", font="Arial, 50")
    weer3datumlabel.grid(column=5, row=8, sticky="nsew", rowspan=2)
    weer3imagelabel.grid(column=6, row=8, sticky="nsew", rowspan=2)
    weer3templabel.grid(column=7, row=8, sticky="nsew", rowspan=2)

    weer4datumlabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[3][0][0]}-{weer[3][0][1]}",
                               font="Arial, 50")
    weer4imagelabel = tk.Label(root, bg="#FFC917", image=images[f"img_{weer[3][1]}"], fg="#003082", text="")
    weer4templabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[3][2]}°C", font="Arial, 50")
    weer4datumlabel.grid(column=5, row=10, sticky="nsew", rowspan=2)
    weer4imagelabel.grid(column=6, row=10, sticky="nsew", rowspan=2)
    weer4templabel.grid(column=7, row=10, sticky="nsew", rowspan=2)

    weer5datumlabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[4][0][0]}-{weer[4][0][1]}",
                               font="Arial, 50")
    weer5imagelabel = tk.Label(root, bg="#FFC917", image=images[f"img_{weer[4][1]}"], fg="#003082", text="")
    weer5templabel = tk.Label(root, bg="#FFC917", fg="#003082", text=f"{weer[4][2]}°C", font="Arial, 50")
    weer5datumlabel.grid(column=5, row=12, sticky="nsew", rowspan=2)
    weer5imagelabel.grid(column=6, row=12, sticky="nsew", rowspan=2)
    weer5templabel.grid(column=7, row=12, sticky="nsew", rowspan=2)

    # review
    if len(reviews) == 0:
        review7berichtlabel = tk.Label(root, bg="#FFC917",
                                       fg="#070721", text=f'Er zijn nog geen reviews voor dit station',
                                       font="Arial, 25", wraplength=850)
        review7naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D", text=f"-.........", font="Arial 15", anchor="e")
        review7berichtlabel.grid(column=0, row=4, columnspan=2, rowspan=2, sticky="nsew")
        review7naamlabel.grid(column=2, row=5, columnspan=2, sticky="nesw")
    if len(reviews) >= 1:
        review1berichtlabel = tk.Label(root, bg="#FFC917",
                                       fg="#070721", text=f'"{reviews[0][0]}"',
                                       font="Arial, 25", wraplength=850)
        review1naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D", text=f"-{reviews[0][1]}", font="Arial 15",
                                    anchor="e")
        review1berichtlabel.grid(column=0, row=4, columnspan=2, rowspan=2, sticky="nsew")
        review1naamlabel.grid(column=2, row=5, columnspan=2, sticky="nesw")
    if len(reviews) >= 2:
        review2berichtlabel = tk.Label(root, bg="#FFC917",
                                       fg="#070721", text=f'"{reviews[1][0]}"',
                                       font="Arial, 25", wraplength=850)
        review2naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D", text=f"-{reviews[1][1]}", font="Arial 15",
                                    anchor="e")
        review2berichtlabel.grid(column=0, row=6, columnspan=2, rowspan=2, sticky="nsew")
        review2naamlabel.grid(column=2, row=7, columnspan=2, sticky="se")
    if len(reviews) >= 3:
        review3berichtlabel = tk.Label(root, bg="#FFC917",
                                       fg="#070721", text=f'"{reviews[2][0]}"',
                                       font="Arial, 25", wraplength=850)
        review3naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D", text=f"-{reviews[2][1]}", font="Arial 15",
                                    anchor="e")
        review3berichtlabel.grid(column=0, row=8, columnspan=2, rowspan=2, sticky="nsew")
        review3naamlabel.grid(column=2, row=9, columnspan=2, sticky="se")
    if len(reviews) >= 4:
        review4berichtlabel = tk.Label(root, bg="#FFC917",
                                       fg="#070721", text=f'"{reviews[3][0]}"',
                                       font="Arial, 25", wraplength=850)
        review4naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D", text=f"-{reviews[3][1]}", font="Arial 15",
                                    anchor="e")
        review4berichtlabel.grid(column=0, row=10, columnspan=2, rowspan=2, sticky="nsew")
        review4naamlabel.grid(column=2, row=11, columnspan=2, sticky="se")
    if len(reviews) >= 5:
        review5berichtlabel = tk.Label(root, bg="#FFC917",
                                       fg="#070721", text=f'"{reviews[4][0]}"',
                                       font="Arial, 25", wraplength=850)
        review5naamlabel = tk.Label(root, bg="#FFC917", fg="#39394D", text=f"-{reviews[4][1]}", font="Arial 15",
                                    anchor="e")
        review5berichtlabel.grid(column=0, row=12, columnspan=2, rowspan=2, sticky="nsew")
        review5naamlabel.grid(column=2, row=13, columnspan=2, sticky="se")

    tijd()
    root.mainloop()


MakeGui()
