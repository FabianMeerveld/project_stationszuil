# Deze module vraagt op het station via de cli aan de gebruiker om een bericht en de naam, vervolgens kiest deze een
# willekeurig station uit en wordt de huidige datum en tijd toegevoegd en wordt dit allemaal opgeslagen in een regel
# van een bestand


import datetime
import random


# functie die vraagt naar het bericht, controleert of deze korter is dan 140 tekens en of het bericht leeg is en
# vervolgens het bericht terug geeft
def get_message():
    while True:
        message = input("Laat hier uw bericht achter. (maximaal 140 tekens) \n")
        if len(message) > 140:
            print("Uw bericht is te lang.")
            continue
        elif len(message) == 0:
            print("Uw bericht mag niet leeg zijn.")
            continue
        else:
            return message


# functie die vraag naar de naam en deze terug geeft, als geen naam wordt ingevoerd dan wordt de naam anoniem terug
# gegeven
def get_name():
    name = input("Wat is uw naam? Laat dit veld leeg om anoniem te blijven. \n")
    if name == "":
        name = "Anoniem"
    return name


# functie die de huidige datum en tijd terug geeft
def get_date():
    date = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
    return date


# functie die een willekeurige lijn uit een bestand met stations vraagt en deze terug geeft
def get_station():
    station_file = open("Stations.txt", "r")
    station_list = station_file.readlines()
    station = station_list[random.randint(0, (len(station_list) - 1))]
    return station


# functie die de gegevens wegschrijft in een bestand (nog fixen dat als er een comma in zit het blijft werken)
def write_stations(message, name, date, station):
    data = f'{message},{name},{date},{station}'
    review_file = open("Review.csv", "a")
    review_file.write("\n"+data)
    print(message, name, date, station)


# loop die constant de data opvraagt en deze vervolgens weg stuurt om op te slaan
while True:
    write_stations(get_message(), get_name(), get_date(), get_station())
    print("Bedankt voor uw bericht!")
