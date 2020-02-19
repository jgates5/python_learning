#dictionary view objects allow us to do is they allow
#  us to peek in and view the values the keys and all of the different
#  items inside of dictionaries.

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

#print(players.keys()) #(['ss', '2b', '3b', 'DH', 'OF'])
#print(players.values()) #['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])

#player_names = list(players.copy().value())


teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}
#nested items
team_groups = teams.items()
print(list(team_groups)) 
print(list(team_groups)[1][1]) 
print(list(team_groups)[1][1][0]) 

#[('astros', ['Altuve', 'Correa', 'Bregman']), 
# ('angels', ['Trout', 'Pujols']), 
# ('yankees', ['Judge', 'Stanton']), 
# ('red sox', ['Price', 'Betts'])]

#('angels', ['Trout', 'Pujols'])
#['Trout', 'Pujols']
#Trout