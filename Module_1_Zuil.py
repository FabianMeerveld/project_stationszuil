import datetime
import random


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


def get_name():
    name = input("Wat is uw naam? Laat dit veld leeg om anoniem te blijven. \n")
    if name == "":
        name = "Anoniem"
    return name


def get_date():
    date = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
    return date


def get_station():
    station_file = open("Stations.txt", "r")
    station_list = station_file.readlines()
    station = station_list[random.randint(0, (len(station_list) - 1))]
    return station


while True:
    data = get_message() + "," + get_name() + "," + get_date() + "," + get_station()
    print("Bedankt voor uw bericht!")
