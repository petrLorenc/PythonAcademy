film = {
    'name': 'Forrest Gump',
    'made': 1994,
    'director': 'Robert Zemeckis',
    'soundtrack': 'Multiple',
    'starring': 'Tom Hanks',
    'fun_fact': '''The house used in Forrest Gump
is the same house used in The Patriot (2000).
Some paneling was changed forinterior shots
in the latter film.'''
}

# print key value

idx = 0
keys = list(film.keys())
while idx < len(keys):
    print('Key: ' + str(keys[idx]) + ' | Value: ' + str(film[keys[idx]]))
    idx += 1

print()
print()
# OR

for key, value in film.items():
     print('Key: ' + str(key) + ' | Value: ' + str(value))

print()
print()
# OR

print()
print()

while film:
    info = film.popitem()
    print('Key: ' + str(info[0]) + ' | Value: ' + str(info[1]))

# Keep in mind that in dictionaries key-value pairs are not ordered at least up to Python 3.5. From Python 3.6 dictionary values are already ordered.

