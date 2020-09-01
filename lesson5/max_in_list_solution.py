# ask user for sequence of integers, use 'q' to quit from asking user for next number

numbers = []
user_input = input("Give a number to save it to list ('q' to quit):")

while user_input != "q":
    numbers.append(int(user_input))
    user_input = input("Give a number to save it to list ('q' to quit):")

# get maximum, minimum and average of the integers in a list without a build in functions
maximum = numbers[0]
minimum = numbers[0]
average = 0
length = 0

for i in numbers:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i
    average += i
    length += 1

print()
print()
print(f"Maximum is {maximum}, minimum is {minimum} and average is {average/length}")

# create immutable copy a list and clear original data

copy_numbers = tuple(numbers)
while len(numbers) and numbers.pop():
    pass

print(copy_numbers)
print(numbers)