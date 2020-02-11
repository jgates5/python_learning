"""So what that is going to do is it's going to take each one 
of these values and it's going to multiply the commission rate by the product cost. And that's 
going to give us our commission value. It's going to add that onto the product cost. So essentially 
this is a system that is trying to see how much money a salesperson should make every time a product 
gets sold. And that's what this will do. It's going to say This product may have cost 88.40 but we also 
have to pay the salesperson 8 percent. So we want the total product cost including the commission. So 
that's what that will equal and then we're going to multiply that by how many units were sold which in
 this case is 450. So I'm going to run that and the value that we get right here is 42962.4"""

#calling from the decimal library of a specific decimal
from decimal import Decimal

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450


product_cost += (commission_rate *product_cost)
print(product_cost * qty) # 42962.4
