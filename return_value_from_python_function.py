"""
def full_name(first, last):
    print(f'{first} {last}')
#print function onlys allows you to see what the syntax error is if your trying to locate something.
full_name('Kristine', 'Hudgens')
"""
#understanding output and input process
#input is the aruguements first and last name, output is nothingneed a return statement ouput.

def full_name(first, last):
    return f'{first} {last}'
#return values show the results in te real world
Kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
    print(f'Hi {name}!')

greeting(Kristine)
#Hi Kristine Hudgens!