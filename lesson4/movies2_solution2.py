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

films_dictionary = []
DIVIDER = '=' * 76

films_dictionary.append(film1)
films_dictionary.append(film2)
films_dictionary.append(film3)
films_dictionary.append(film4)

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

print("Films in our database:")
print(f'OPTIONS: 0 - {films_dictionary[0]["NAME"]}| 1 - {films_dictionary[1]["NAME"]}, 2 - {films_dictionary[2]["NAME"]} : 2, {films_dictionary[3]["NAME"]} : 3')

if choice == "all films" or choice == 1:
    # ALL FILMS - show all films
    all_films = films_dictionary[0].get('NAME') + "|"
    all_films = all_films + films_dictionary[1].get('NAME') + "|"
    all_films += films_dictionary[2].get('NAME') + "|"
    all_films += films_dictionary[3].get('NAME')
    print(all_films)

elif choice == "details of film" or choice == 2:
    # DETAILS OF FILM  - ask for which one and the show all his information
    selected_film = input("Which film from our database are you after? ")
    if selected_film == "Shawshank Redemption":
        print("The following are the film's details:", films_dictionary[0])
    elif selected_film == "The Godfather":
        print("The following are the film's details:", films_dictionary[1])
    elif selected_film == "The Dark Knight":
        print("The following are the film's details:", films_dictionary[2])
    else:
        print("The following are the film's details:", films_dictionary[3])

elif choice == "actor intersection" or choice == 3:
    # ACTOR INTERSECTION - between two chosen films
    film1 = input('What is the first film you would like to compare? (please enter as a number from 0 to 3): ')
    film2 = input('What is the second film you would like to compare? (please enter as a number from 0 to 3): ')
    actors1 = set(films_dictionary[int(film1)]['ACTORS'])
    actors2 = set(films_dictionary[int(film2)]['ACTORS'])
    print('The actors common to both films are: {}'.format(actors1 & actors2))
elif choice == "all directors" or choice == 4:
    # ALL DIRECTORS - show unique names of all directors in our database
    i = 0
    directors = set()
    while i < len(films_dictionary):
        directors.add(films_dictionary[i]['DIRECTOR'])
        i += 1
    print(directors)
