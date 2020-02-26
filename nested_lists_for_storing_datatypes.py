users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']
ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]
print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)

nested_lists = [[123], [234], 345]] most basic list possible

teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1])