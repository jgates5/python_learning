"""they're going to all focus around how 
one set can interact with another one"""

tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

#merge tags
#merged_tags = tags_one | tags_two
#print(merged_tags) 
# merging tags {'python', 'coding', 'development', 'ruby', 'tutorials'}

#exclusive_to_tag_one = tags_one - tags_two
#print(exclusive_to_tag_one) 
#{'python'}
#tags in tags_one but not in tags_two
#have a master type of set and subtract the other items

#tags in tags_two but not in tags_one
exclusive_to_tag_two = tags_two - tags_one
print(exclusive_to_tag_two) 
#{'ruby', 'development'}
#ruby and development are in tags two but not in tags one

#tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two
print(universal_tags) #{'development', 'ruby'}
#{'tutorials', 'coding'} -> they are only universal between the two tags