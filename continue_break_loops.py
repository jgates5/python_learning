#2 different flow operators 1 is break and 1 is continue

usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]
#search for Cersei of who this person is continue what represents
for username in usernames:
    if username == 'cersei':
        print(f'{username} was found at index {usernames.index(username)}')
        break
    print(username)
"""
        print(f'Sorry, {username}, you are not allowed')
        continue#<- tells to continue through the loop
    else:
        print(f'{username} is allowed')
"""
"""
jon is allowed
tyrion is allowed
theon is allowed
Sorry, cersei, you are not allowed
sansa is allowed
"""