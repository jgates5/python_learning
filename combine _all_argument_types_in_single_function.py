def greeting(time_of_day, *args, **kwargs):


#def greeting, I'm going to start off with a positional 
#arguments you say time of day then I'm going to give a 
#single Asterix here and to say args by following the common 
#convention and this is going to take in the user's name and 
#then I'm going to work with keyword arguments so we're going 
#to use double asterisks kwargs and then from there we are going
#to provide the function body.

    print(f"Hi {' '.join(args)}, I hope that you are having a great {time_of_day}")

    if kwargs:
        print('Your tasks for the day are:')
        for key, val in kwargs.items():
            print(f"{key} => {val}")


greeting('Morning',
         'Krsitine', 'Hudgens',
         first = 'Emtpy dishwasher',
         second = 'take pupper outside',
         third = 'Math homework')
"""
 And so I'm going to start off with the traditional print statement so 
 I'll use a formatted string here so I'll say f and then Hi and then inside 
 of this I'm going to use a string literal and pass in a joint statement 
 """

"""So I'm going to join the args which is going to take in the full set of arguments and this is
 going to be the user's name. So this could be their first name, their first and last name, their
  first middle and last name, it doesn't matter it will work for any type of user. So say hi and then print out their name and then I'll say I hope you are having a great and then put inside the time of day and that will end our greeting.
  """