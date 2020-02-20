#a list uses  brackets[]
# a dictionary uses curly braces{}
# a tuple uses parentheses ()

#tuple:imutable cant use post.sort() 
#list: mutable, is this a data structure i need to change or is it something i want to keep the same?
post = ('Python Basics', 'Intro guide to python', 'Some cool python content')



#we are using an index and storing that number inside of a variable
#this is the same as 
"""title =post[0]
sub_heading =post[1]
content =post[2]"""

#always using List can cause bugs in your code
post = ['Python Basics', 'Intro guide to python', 'Some cool python content']
 #but what if I use
post.sort() 
"""Intro guide to python
Python Basics
Some cool python content"""

#unpacking technique -> title, sub_heading, content = post
title, sub_heading, content = post
print(title)
print(sub_heading)
print(content)

