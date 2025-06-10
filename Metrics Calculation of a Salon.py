# the data from a hair salon
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# how many times each cut was sold last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# calculating the average price
number_of_prices = len(prices)
total_price = sum(prices)
average_price = total_price / number_of_prices
print(average_price)

# reducing each price by $5
new_prices = [reduced_price - 5 for reduced_price in prices]
print(new_prices)

# calculating total revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  print(total_revenue)

# this calculates the average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# this finds all cuts that are under $30
cuts_under_30 = 0
for cuts in prices:
  if cuts < 30:
    print(cuts)