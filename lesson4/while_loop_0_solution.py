# Creating the shopping cart
cart = []

# 1. Ask the user for 3 prices (numbers),
item1 = float(input('Enter the price (1/3): '))
item2 = float(input('Enter the price (2/3): '))
item3 = float(input('Enter the price (3/3): '))

# 2. Add them into a list representing the shopping cart,
cart.append(item1)
cart.append(item2)
cart.append(item3)

# 3. Calculate the total price,
total_price = cart[0] + cart[1] + cart[2]

# 4. Print the cart content and the total price.
print('CART: ' + str(cart))
print('Total Price: ' + str(total_price))