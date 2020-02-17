teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}
#looking up mets is not in the lis of dictionary
#using get calling on the teams dictionary collecting two arguments
featured_team = teams.get['mets', 'No featured team']

print(featured_team)