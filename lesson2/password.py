name = "Petr"
year = 1999
password = input("Password:")

valid = True

if len(password) < 8:
    print("Password has to be 8 character long.")
    valid = False
if name in password:
    print("You cannot use your name.")
    valid = False
if str(year) in password:
    print("You cannot use your year of birth.")
    valid = False
if password.isalpha() and not password.isnumeric():
    print("Password does not contain numbers.")
    valid = False
if not password.isalpha() and password.isnumeric():
    print("Password does not contain letters.")
    valid = False
if not password.isalnum():
    print("Password has to be made only from numbers or letters.")
    valid = False

if valid:
    print("Password is correct.")
