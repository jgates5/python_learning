from decimal import Decimal

product_cost = 88.80
commision_rate = 0.08
qty = 450 #<- integer

#convert product_cost to an integrer
print(int(product_cost)) #88

#convert qty to a float
print(float(qty))#450.0

#convert Decimal from decimal library
print(Decimal(product_cost))#88.7999999999999971578290569595992565155029296875
#converting complex
print(complex(product_cost))#(88.8+0j)
