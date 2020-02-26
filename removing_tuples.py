post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

#removing elements from end
# implement reassignment
#remove tuples from the end
#post = post[:-2] ('Python Basics', 'Intro guide to Python', 'Some cool python content')

#remove elements from beginning, grabbing all the elements after the first element.
#psot = post[1:]
#print(post)

#removing specfic elemetn (messy/not recommended)
post = list(post) #['Python Basics', 'Intro guide to Python', 'Some cool python content', 'published']
#now we can remove items from list
post.remove('published')
post = tuple(post)
print(post)