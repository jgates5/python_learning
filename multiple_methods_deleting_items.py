teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

#most basic way to delete an item from a dictionary

#del teams['astros']
#print(teams)
#Results = {'angels': ['Trout', 'Pujols'], 
# 'yankees': ['Judge', 'Stanton'], 
# 'red sox': ['Price', 'Betts']}

#using get function
#print(teams.get('mets', 'No team found by that name'))
#results = No team found by that name

"""using pop to delete the dictionary
teams.pop('astros', 'No team found by that name')
print(teams) = {'angels': ['Trout', 'Pujols'], 
'yankees': ['Judge', 'Stanton'], 
'red sox': ['Price', 'Betts']}
"""

#typing in a key and a name that does not exist
#teams.pop('rays', 'No team found by that name')
#print(teams)
#returns no defalt value or returns the default element

#typing in a key and a name that does not exist
removed_team= teams.pop('rays', 'No team found by that name')
print(teams)
print(removed_team)
