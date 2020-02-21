post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

#Adding the nested elements to the end of the list
tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post)
print(post[-1][-1])