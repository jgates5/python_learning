tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
    'computer science'
]

#Ranges and slices going to end before computer science
tag_range = tags[1:-1]

#adding  third element interval with every other tag
#tag_range = tags[:-1:2] the answer is it grabs [python, tutporials, and prgramming]
#this tag range will flip the order of the list around for computer science to be first, then programming and so forth
tag_range = tags[::-1]
print(tag_range)
#there is a key difference how the sorting function works
#sort looks at the alphabetical value that calls the first letter in the list that is the last beginning letter in the alphabetical
#so t as in tutorials pulled the call value first then python and so forth.
#tags.sort(reverse=True)
#['tutorials', 'python', 'programming', 'development', 'computer science', 'code']
#sorting function can be tricky.
#call out function sorted tags
"""Sort does not return anything. Sort will go in and revserse them, sort the list alphabetically and change tags
but it will not return that value. the sort function goes in and changes tags, but doesnt store it as a standard operation inside a variable.
if you try to assign it, its not going to give  you a value"""

sorted_tags = tags.sort(reverse=True)
print(sorted_tags)
