numbers = [1, 2, 3, 4, 5, 6, 10]

# sum all power of numbers in list
result = 0
for x in numbers:
    result += x ** 2

print(result)

# sum all power of numbers in list
result = 0
for x in numbers:
    result += 2 ** x

print(result)

# how many numbers are divisible by 2

result = 0
for x in numbers:
    result += not bool(x % 2)

print(result)