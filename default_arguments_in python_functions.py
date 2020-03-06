"""
def greeting(name = 'Guest'): #having a deafult name of the unidentified user place in with name
    print(f'Hi {name}!')
greeting()#prints out hi guest when no arguments are accounted for
greeting('Kristine')#but when you do pass in a string this over rides the default
#common interview question
"""
"""
def some_function(collection = []):
    collection.append(1)
    return collection
print(some_function())#[1]
print(some_function())
"""
"""
if you're calling some function from some other part of the program it is going 
to go back and it's going to see the very first time where collection was created and it's
 going to go reference that original collection. So even though your other part of the program thought 
 it was starting off with a clean slate. It was just calling some function and performing some type of behavior. 
 You actually have a connection between the two collections.
#mutability vs immunibility, you do not want to do a mutaible data type
"""
def some_function(collection = []):
    collection.append(1)
    print(id(collection))
    return collection

print(some_function())#[1]
print(some_function())
"""
And so now if I run this again you're going to see that when we print it out some function 
the first time that it printed out this long number it ends in 776. When we printed out the sum function 
somewhere else in the program it is still pointing to that 776 address in your computer's memory. And that 
is the reason why we have a list that did not start off with the clean slate but it actually added onto it.

And so that is the reason why it is considered a very bad practice to ever set a default argument as a list.
"""