#Leveraging reassignment
# adding a Tuple in parenthesis
#post = post + ('published',) 
#need to add a [,] to make it a tuple
# can only concatenate tuple (not "str") to tuple


post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))
#post = post + ('published',) 
post += ('published',) #-> """
create two objects add them together so we're concatenating them and then 
put them inside of this variable and it's simply going to override it.
"""
print(id(post))
#title, sub_heading, content, status = post

"""
print(title)
print(sub_heading)
print(content)
print(status)
"""
"""Python Basics
Intro guide to python
Some cool python content
published"""

"""post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))

post += ('published',)

print(id(post))

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)
"""