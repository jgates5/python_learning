import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]
"""
sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
beginning_priced_items = sorted_list[:math.floor(num_of_sales/2)]
median = sorted_list[math.floor(num_of_sales/2):(math.floor(num_of_sales/2)+1)]
print(sorted_list)
print(num_of_sales)
print(beginning_priced_items)
print(median)
"""
list_prices = sorted(sale_prices)
total_of_sale_items = len(list_prices)
half_slice = math.floor(num_of_sales/2)
median = list_prices[half_slice:(half_slice +1)]
print(list_prices)
print(total_of_sale_items)
print(median)