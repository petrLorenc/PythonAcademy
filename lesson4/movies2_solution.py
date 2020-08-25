# declare dict film
film1 = {"NAME": "Shawshank Redemption",
         "RATING": "93/100",
         "YEAR": 1994,
         "DIRECTOR": "Frank Darabont",
         "LENGTH": 144,
         "ACTORS": (
             "Tim Robbins",
             "Morgan Freeman",
             "Bob Gunton",
             "William Sadler",
             "Clancy Brown",
             "Gil Bellows",
             "Mark Rolston",
             "James Whitmore",
             "Jeffrey DeMunn",
             "Larry Brandenburg"
         )}

film2 = {
    "NAME": "The Godfather",
    "RATING": "92/100",
    "YEAR": 1972,
    "DIRECTOR": "Francis Ford Coppola",
    "LENGTH": 175,
    "ACTORS": (
        "Marlon Brando",
        "Al Pacino",
        "James Caan",
        "Richard S. Castellano",
        "Robert Duvall",
        "Sterling Hayden",
        "John Marley",
        "Richard Conte"
    ),
}

film3 = {
    "NAME": "The Dark Knight",
    "RATING": "90/100",
    "YEAR": 2008,
    "DIRECTOR": "Christopher Nolan",
    "LENGTH": 152,
    "ACTORS": (
        "Christian Bale",
        "Heath Ledger",
        "Aaron Eckhart",
        "Michael Caine",
        "Maggie Gyllenhaal",
        "Gary Oldman",
        "Morgan Freeman",
        "Monique Gabriela",
        "Ron Dean",
        "Cillian Murphy"
    ),
}

film4 = {
    "NAME": "The Prestige",
    "RATING": "85/100",
    "YEAR": 2006,
    "DIRECTOR": "Christopher Nolan",
    "LENGTH": 130,
    "ACTORS": (
        "Hugh Jackman",
        "Christian Bale",
        "Michael Caine",
        "Piper Perabo",
        "Rebecca Hall",
        "Scarlett Johansson",
        "Samantha Mahurin",
        "David Bowie"
    )
}

films_dictionary = {}
DIVIDER = '=' * 76

films_dictionary[film1["NAME"]] = film1
films_dictionary[film2["NAME"]] = film2
films_dictionary[film3["NAME"]] = film3
films_dictionary[film4["NAME"]] = film4

print(DIVIDER)
print("Our film database")

print(
    f"""{DIVIDER}
OPTIONS: '1 - ALL FILMS | 2 - DETAILS OF FILM | 3 - ACTOR INTERSECTION | 4 - ALL DIRECTORS'
{DIVIDER}"""
)

choice = input("Choice: ").lower().strip()

if choice.isnumeric():
    choice = int(choice)

if choice == "all films" or choice == 1:
    print(DIVIDER)
    print(f"All films:")
    print(list(films_dictionary.keys()))
    print(DIVIDER)

elif choice == "details of film" or choice == 2:
    print(DIVIDER)
    print(list(films_dictionary.keys()))
    print(DIVIDER)

    vyber_filmu = input("Which one: ")
    print(DIVIDER)
    print(films_dictionary.get(vyber_filmu, "Not found!"))

elif choice == "actor intersection" or choice == 3:
    print(DIVIDER)
    print(list(films_dictionary.keys()))
    print(DIVIDER)

    film1 = input("CHOOSE I. FILM: ")
    film2 = input("CHOOSE II. FILM: ")

    herci_film1 = set(films_dictionary[film1]["ACTORS"])
    herci_film2 = set(films_dictionary[film2]["ACTORS"])

    prunik = herci_film1 & herci_film2
    print(f"ACTOR INTERSECTION FOR *{films_dictionary[film1]['NAME']}* AND *{films_dictionary[film2]['NAME']}*: {prunik}")

elif "all directors" in choice or choice ==4:
    print(DIVIDER)
    set_reziseri = (
        films_dictionary["The Dark Knight"]["DIRECTOR"],
        films_dictionary["The Godfather"]["DIRECTOR"],
        films_dictionary["Shawshank Redemption"]["DIRECTOR"],
        films_dictionary["The Prestige"]["DIRECTOR"]
    )

    print("ALL DIRECTORS:")
    print(f"{set(set_reziseri)}")
else:
    print("UNKNOWN CHOICE")