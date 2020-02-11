#heading = "Python: An Introduction, and Python: Advanced" #pretend this is a heading on a website
#3 variables available
#The way that the partition function works in Python is it's going to look inside the string for whatever you pass in as the argument
#returns a tupil collection. one string into 3 string, variable deconstruction.
#header, _, subheader = heading.partition(': ')
#irst, second, third = heading.partition(': ')
#print(first)
#print(second)
#print(third)

#The important component to remember whenever 
#you're working with partition is that it breaks 
#whatever you pass in. So what we have right here this kind of 
#sentinel value with what we have with the colon and a space. 
#It's good to pass that into the string it's going to try to find it and then it's going to return three elements. 
#It does not matter how big the string is that you pass to partition.


#tags = 'python,coding,programming,development'

#list_of_tags = tags.split(',') #-> creates a list
#list_of_tags = tags.split() # -> creates a single string

#print(list_of_tags)


heading = "Python: An Introduction"

heading, subheading = heading.split(': ')

print(heading)
print(subheading)