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
#grabbing just astros
"""print(teams[0])
{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}"""

"""angels = teams[1].get('angels', 'Team not found')
print(list(angels.values()))"""

angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1]) #= Pujols