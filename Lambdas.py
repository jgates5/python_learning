"""
 is a tool that allows you to wrap up a function. Usually, 
 a smaller function and then easily pass it to other functions. 
 Now functions inside a python are what are called first-class citizens
which means that you can treat a function like any type of object.wrap up small behavior then pass it to other functions.
"""
# a lambda returns a value and store it in the full-name variable.
#full_name = lambda first, last: f'{first} {last}'
"""
def gretting(name):
    print(f'Hi there {name}')

greeting(full_name('Kristine', 'Hudgens'))
"""

full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))

#what ever comes after the colun that is the behavior that is going to be returned.