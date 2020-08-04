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
DISCOUNT_25 = ['Svitavy', 'Ostrava']

# Check, whether entered valid input
if not 0 < selection <= len(DESTINATIONS):
    print('We are sorry, but we can offer only those ' + str(len(DESTINATIONS)) + ' destinations')
else:
    # Get data from variables based on user's input
    destination = DESTINATIONS[selection - 1]
    price = PRICES[selection - 1]
    # Calculate the price & check whether discount applicable for the selected destination
    if destination in DISCOUNT_25:
        print('Lucky you! You have just earned 25% discount for your destination - ' + destination)
        input('Press enter to continue')
        price = price * 0.75
    print('=' * 80)

# Introduce registration
print('registration:'.upper())
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

# Check if the user is older than 15 years old
if 2020 - int(birth_year) < 15:
    print('Sorry, we cannot offer our services to babies')

# Check if email contains @ symbol
elif '@' not in email:
    print('Sorry, you have provided incorrect email')

# Check if password
# - is at least 8 chars long,
# - doesn't begin and end with a number
# - and contains both letters and numbers
elif (password.isnumeric() or password.isalpha()
      or password[0].isnumeric() or password[-1].isnumeric()
      or len(password) < 8):
    print('''
	Our passwords have to:
	* contain numbers and letters
	* be min 8 chars long
	* cannot begin or end with digit

	We cannot accept your password
	''')

else:
    # Thank user by the input name and inform him/her about the reservation made
    print('Thank you ' + name)
    print('We have made your reservation to ' + destination)
    print('The total price is ' + str(price))
