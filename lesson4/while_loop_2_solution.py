# 1. Create the cart
cart = []

# 2. Adding new prices to the cart - allow infinite adding and quit by user
quit_signal = ""
while True:
    item = input('Enter the price or "q" for quit: ')
    if item == "q":
        break
    cart.append(float(item))

# 3. List the cart's content - list items one by one until the user enters letter 'q'
repetition = 0
quit_signal = ""
while quit_signal != "q":
    index = repetition % len(cart)
    print("Item no. " + str(index) + ": " + str(cart[index]))
    quit_signal = input('Press enter to continue or "q" to quit: ')
    repetition = repetition + 1

# 4. Calculate the total price
total_price = 0
index = 0
while index < len(cart):
    total_price = total_price + cart[index]
    index = index + 1

# 5. Print the cart's content
print('CART: ' + str(cart))

# 6. Print the total price
print('Total Price: ' + str(total_price))
