# declare empty dict film
film = {}

# populate the film dict
film['name'] = 'Shawshank Redemption'
film['rating'] = 87
film['year'] = 1994
film['director'] = 'Frank Darabont'

# update the film dict
film.update(starring=['Tim Robbins', 'Morgan Freeman'])
film.update({"budget": 200})
film.update({"budget": 100})

print(film)
# erase the budget key
del film['budget']

# declare empty dict films
films = {}

# add the film dict into films dictionary
films.update(DRAMA=film)

# print the offer
print('We can currently offer:')
print(list(films))

# ask the user for genre
genre = input('What genre are you interested in? ')
print()

# print the films stored under the selected category
print('HERE IT GOES')
print(films[genre])

# clear the films database and print the result
films.clear()
print('DATABASE HAS BEEN ERASED:')
print(films)
