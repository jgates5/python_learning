def greeting(**kwargs):#keywords acronym KW- unpacking
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")

greeting(first_name = 'Kristine', last_name = 'Hudgens')
#pass in some named arguments
#greeting(first = 'Kristine', last = 'Hudgens')
"""
def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens')
"""