"""
a list is similar to an array.
a list is like a set of collection of data
you can sort the, see their collections, keep list data types asformal as possible.
Now a list in Python if you're coming from other programming languages is like an array. 
It is a collection of values and that collection can be added to. You can remove items. 
You can query elements inside of it.
"""

"""
User database Query
Kristine
Tiffany
Jordon
"""
users = ['Kristine', 'Tiffany', 'Jordon']

print(users)

#Placing a new element in the list then give it an index and a value
users.insert(0, 'Anthony')
        #index^ so anthony will be first in the list
        
#use append by adding another element to the end of a list
users.append('Ian')
print(users)

#each list object you can call to the list data type but you can call that specific item
print(users[2])

#to call Tiffany with brackets in its own list you need to say 
print([users[2]]) 

#to edit a value in a list and replace it with another value find the index then call the value for a replacement of another value
users[4] = 'Brayden'
print(users)
