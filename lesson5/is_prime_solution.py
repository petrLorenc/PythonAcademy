number = int(input("Give a number to test if it is prime?"))

is_prime = True

for x in range(2, number):
    if number % x == 0:
        is_prime = False
        break

if is_prime:
    print("The number is prime number.")
else:
    print("The number is not prime number.")