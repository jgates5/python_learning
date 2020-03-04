# the IN operator checked to see if an operator is inside another element
"""
sentence = 'The quickbrown fox jumped over the lazy Dog'
word = 'quick'
if word in sentence:
    print('The word was found in the sentence')
else:
    print('The word was not in the sentence')
#The word was found in the sentence
"""
"""
sentence = 'The quickbrown fox jumped over the lazy Dog'
word = 'dog'
if word in sentence:
    print('The word was found in the sentence')
else:
    print('The word was not in the sentence')
#The word was not in the sentence
"""
"""
sentence = 'The quickbrown fox jumped over the lazy Dog'
word = 'quick'

if word.lower() in sentence.lower():

    print('The word was found in the sentence')
else:
    print('The word was not in the sentence')
#The word was found in the sentence
"""

nums = [1, 2, 3, 4]
if 3 in nums: #is this in nums
    print('The number was found')
else:
    print('The number was not found')
#The number was not found