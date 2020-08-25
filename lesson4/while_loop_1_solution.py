# Creating the shopping cart
cart = []

# 1. Ask the user for 3 prices (numbers),
# 2. Add them into a list representing the shopping cart,
idx = 1
while idx <= 3:
    cart.append(float(input(f'Enter the price ({idx}/3): ')))
    idx += 1

# 3. Calculate the total price,
idx = 0
total_price = 0
while idx < len(cart):
    total_price += cart[idx]
    idx += 1

# 4. Print the cart content and the total price.
print('CART: ' + str(cart))
print('Total Price: ' + str(total_price))