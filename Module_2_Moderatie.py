import datetime
import psycopg2

def Make_connenction():
    host = '20.160.193.51'
    port = 5432
    name = 'stationszuil'
    user = 'postgres'
    password = 'Bami'
    info_string = f"host='{host}' port='{port}' dbname='{name}' user='{user}' password='{password}'"
    connection = psycopg2.connect(info_string)
    return connection



def Post_review(time, email, review, goedkeuring):
    print("1")


def Get_date():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return date




def Get_name(email):
    connection = Make_connenction()
    cursor = connection.cursor()
    query = f"""SELECT naam
                FROM moderator
                WHERE email = '{email}'
                """
    cursor.execute(query)
    records = cursor.fetchall()
    if len(records) == 0:
        while True:
            naam = input("Wat is uw naam: ")
            if naam == "":
                print("Uw naam mag niet leeg zijn")
                continue
            else:
                query1 = """INSERT INTO moderator(naam, email) VALUES (%s,%s)"""
                data = (naam,email)
                cursor.execute(query1,data)
                connection.commit()
                break
    else:
        naam = records[0][0]
    connection.close()
    return naam


def Get_review():
    file = open("Review.csv")
    lines = file.readlines()
    file.close()
    if len(lines) < 1:
        print("Er zijn geen reviews om beoordeeld te worden")
        review = "break"
    else:
        review = lines[0].split(";")
    return review


def Remove_review(review):
    review = f'{review[0]};{review[1]};{review[2]};{review[3]}'
    file = open("Review.csv", "r")
    lines = file.readlines()
    file.close()
    for index in range(len(lines)):
        if lines[index] == review:
            lines[index] = ""
    file = open("Review.csv", "w")
    file.truncate()
    file.close()
    file = open("Review.csv", "a")
    for x in lines:
        file.write(x)
    file.close()


def Startup():
    review_file = open("Review.csv", "a")
    review_file.close()
    print("Welkom bij de moderatie module")
    while True:
        email = input("Wat is uw email: ")
        if "@" in email and "." in email and not " " in email:
            break
        else:
            print("Voer een geldig email adres in")
            continue
    name = Get_name(email)
    print(f"Welkom {name}")
    while True:
        review = Get_review()
        if review == "break":
            print("Alle reviews zijn beoordeeld, druk op enter om af te sluiten")
            input("")
            break
        else:
            print(
                f"Op {review[0]} schreef {review[2]} op station {review[3].strip()} het volgende bericht:\n{review[1]}")
            print("Kies 1 om het bericht goed te keuren en 2 om het bericht af te keuren")
            while True:
                keuze = input("")
                if keuze == "1":
                    keuze = True
                    break
                elif keuze == "2":
                    keuze = False
                    break
                else:
                    print("input onjuist")
                    continue
            Post_review(Get_date(), email, review, keuze)
            Remove_review(review)


Startup()
