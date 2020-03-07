#def greeting unpacking *args = argument =unpacked or a list that will be past into the function.
"""
def greeting(*args):
    #print('Hi ' + ' '.join(args))#concatinate
    print(args)#working with unpacking or arguments list your working with Tuple data structure

greeting('Tiffany', 'Hudgens')
greeting('Kristine', 'M', 'Hudgens')#passing in three argguments
"""

"""def greeting(*names):#names as an argument works but goes against the python convention. When you go in the source cod ein a program you will see(*args)
    print('Hi ' + ' '.join(names))

greeting('Tiffany', 'Hudgens')
greeting('Kristine', 'M', 'Hudgens')
"""
"""
def greeting(time_of_day, *args): #you can specify the time of day as a second argument
    print('Hi ' + ' '.join(names))
#time of day is taking in the first value of tiffany
greeting('Tiffany', 'Hudgens')
greeting('Kristine', 'M', 'Hudgens')
"""

def greeting(time_of_day, *args): #so we need to change Tiffany to Morning and change Kristine to Afternoon
   # print('Hi ' + ' '.join(args))#then all the values after mornng and afternoon will be wrapped inside the args tuple
#join allows you to take in a collection and joins it turns it into a string then takes in an empty space tuple
#to get the basic concept we can explain what the values mean
    print(f"Hi {' '.join(args)}, I hope that you are having a good {time_of_day}")
greeting('Morning', 'Tiffany', 'Hudgens')
greeting('Afternoon', 'Kristine', 'M', 'Hudgens')

"""Hi Tiffany Hudgens, I hope that you are having a good Morning
Hi Kristine M Hudgens, I hope that you are having a good Afternoon
"""