# Greet the client
print('=' * 80)
print('''Welcome to the DESTINATIO,
place where people plan their trips''')
print('=' * 80)

# Offer destinations
print('We can offer you the following destinations:')
print('-' * 80)
print('''
1 - Prague  | 1000
2 - Wien    | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
''')
print('-' * 80)

# Get input from user about destination
selection = int(input('Please enter the destination number to select: '))

# Assign variables appropriate data
DESTINATIONS = ['Prague', 'Wien', 'Brno', 'Svitavy', 'Zlin', 'Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]

# Get data from variables based on user's input
destination = DESTINATIONS[selection - 1]
price = PRICES[selection - 1]

# Introduce registration
print('=' * 80)
print('REGISTRATION:')
print('-' * 80)
print('In order to complete your reservations, please share few details about yourself with us.')
print('-' * 80)

# Get input from user about personal data
name = input('NAME: ')
print('=' * 40)
surname = input('SURNAME: ')
print('=' * 40)
birth_year = input('YEAR of BIRTH: ')
print('=' * 40)
email = input('EMAIL: ')
print('=' * 40)
password = input('PASSWORD: ')
print('=' * 80)

# Thank user by the input name and inform him/her about the reservation made
print('Thank you ' + name)
print('We have made your reservation to ' + destination)