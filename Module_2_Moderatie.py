import datetime

def Post_name(name, email):
    # post name to database
    return

def Post_review(time, email, review, goedkeuring):
    print("1")
def Get_date():
    date = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
    return date

def Get_name(email):
    name = ""
    # haal naam op uit database
    if name == "": #vraag naar naam als naam niet in database staat
        while True:
            name = input("Wat is uw naam: \n")
            if name == "":
                print("Uw naam mag niet leeg zijn")
                continue
            else:
                Post_name(name, email)
                break
    return name

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
    print("Welkom bij de moderatie module")
    while True:
        email = input("Wat is uw email: \n")
        if "@" in email and "." in email and not " " in email:
            break
        else:
            print("Voer een geldig email adres in")
            continue
    name = Get_name(email)
    while True:
        review = Get_review()
        if review == "break":
            break
        else:
            print(f"Op {review[0]} schreef {review[2]} op station {review[3].strip()} het volgende bericht:\n{review[1]}")
            print("Kies 1 om het bericht goed te keuren en 2 om het bericht af te keuren")
            keuze = input("")
            Post_review(Get_date(),email,review,keuze)
            Remove_review(review)

Startup()