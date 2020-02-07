#replace function then reassign a set value
sentence = 'The quick brown fox jumped over the lazy dog'

#sentence = 'New Value' #sentence variable is = to the above sentence but two diffent strings
sentence = sentence.replace('quick', 'slow') #reassigned  a replacement word quick with slow
print(sentence)