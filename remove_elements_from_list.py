users = ['Krisitne', 'Tiffany', 'Jordon', 'Leann']
print(users)

#users is the list

users.remove('Jordon') #index 2 was jordon

print(users)

#second way to remove a value from a list
popped_user = users.pop() #pop removes the very last element and retruns an item so you can use it
print(popped_user)
print(users)

#3. to pure delete a value in a list pass in a value

del users[0]

print(users)