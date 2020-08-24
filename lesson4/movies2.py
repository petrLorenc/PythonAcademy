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


print(DIVIDER)
print("Our film database")

print(
f"""{DIVIDER}
OPTIONS: 'ALL FILMS | DETAILS OF FILM | ACTOR INTERSECTION | ALL DIRECTORS'
{DIVIDER}"""
)


# ALL FILMS - show all films
# DETAILS OF FILM  - ask for which one and the show all his information
# ACTOR INTERSECTION - between two chosen films
# ALL DIRECTORS - show unique names of all directors in our database
