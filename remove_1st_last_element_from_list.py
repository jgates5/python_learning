"""
remove_first_and_last(list_to_clean)
html = ['<h1>', 'Some content', '</h1>']

remove_first_and_last(html)
=> 'Some content'

html_2 = ['<h1>', 'Some content', 'more', '</h1>]]

remove_first_and_last(html_2) =>'some content', 'more']
"""
# so lets take a list [1,2,3] you can grab these elemnts one, two, three = [1, 2, 3, 4, 5]:
#you can use the blob function to blob everything in the middle
def remove_first_and_last(list_to_clean):
    _, *content, _ =  list_to_clean
    return content

html = ['<h1>', 'Some content', 'more', '</h1>']

print(remove_first_and_last(html))
#['Some content', 'more']

"""
>> one, two, three = [1, 2, 3]
>>> one
1
>>> two
2
>>> three
3
>>> one, *two, three = [1, 2, 3, 4, 5]
>>> one
1
>>> three
5
>>> two
[2, 3, 4]
"""