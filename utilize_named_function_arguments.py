"""def full_name(first, last):
  print(f'{first} {last}')

full_name('Kristine', 'Hudgens')
"""
"""
Kristine string is going to be passed to this first argument and then it's going to be used throughout the entire function because we passed it in as the first element. And so Hudgens is going to be passed into the last value 
"""
def full_name(first, last):
  print(f'{first} {last}')

full_name(first = 'Krsitine', last = 'Hudgens')#can call first name and last or last name first then first name
#using named arguments is best to use than calling it to be specific