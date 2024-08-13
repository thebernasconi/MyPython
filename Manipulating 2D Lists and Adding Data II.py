toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
# How to count how many times an element appears 
num_two_dollar_slices = prices.count(2)
# How to count how many elements in the lsit
num_pizzas = len(toppings)
# Using str() to convert an int into str to concatenate
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
# Sorting the list into crescent numbers order
pizza_and_prices.sort()
print(pizza_and_prices)
# Selecting the first element of a list
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
# Selecting the last element on a list
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# Removing the last element on a list with .pop()
pizza_and_prices.pop()
print(pizza_and_prices)
# Inserting a new element with .insert(position, element)
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
# Slicing a piece off froma list without removing them from the original
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
print(pizza_and_prices)