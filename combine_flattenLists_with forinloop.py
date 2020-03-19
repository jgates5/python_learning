"""
legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]
print(raw_db)
#[['Alice', 'Bob', 'Tiffany', 'Kristine']]
#[['Alice', 'Bob', Tiffany', 'Kristine']]

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)
#['Tiffany', 'Kristine', 'Alice', 'Bob']
""" 
legacy_customers = ['hello', 'hi']
used_product = ['new', 'used']

for x in legacy_customers:
    used_product.append(x)
    
print(used_product)