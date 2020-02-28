"""
A for in loop would be the ability to turn this knob many times but only as many 
times as there are gumballs in here. So in other words, if I have 250 gumballs in 
this machine a for in loop will turn this knob and let a gumball fall out 250 times.
That is a very nice thing about for in loops because you as a developer you don't 
have to keep track or even know how many items are in a list in a tuple or in a dictionary 
you can simply iterate over it. If there is one it will go through it one time, if there are 5,000
 you'll go through 5,000 times.

Now the second type of loop is a while loop. Now a while loop is a very different. It's a 
little bit more low level it's not quite as intelligent as a for in loop a while loop will continue as many 
times as you want it to go. So in other words if we have 250 gumballs in here and I set a while loop to perform 
this task. And I don't tell the while loop when to stop even after I've gone through and I've spun the knob 250 
times the while loop will keep on going. It will do it a thousand times 2000 times they'll keep on going and in fact, 
if you don't implement a while loop properly then you will run into what's called an infinite loop where the program will never 
stop and eventually the computer or the server will just crash.
What you have to do when working with a while loop is you as a developer need to actually tell it when to stop. 
"""
#looping through each one of these i would use a for in loop
#players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
#for player in players: #players is plural whenever using for in loops
"""#this first variable right here this is a block variable or an iterator variable 
depending on your preference. With this, this could be named anything. And so there's nothing specific about using the word player here.
If I said X and then change this to x then this would still work.
But this player variable here this block variable is going to be equal to Altuve. Then when the for loop goes 
through again then the player variable is going to be equal to Bregman. Then it's going to be Correa and then Gattis and so on so 
forth if you had a million items that you were iterating over the player value here would change a million times."""
   # print(player) #Altuve, Bregman, Correa, Gattis


#changing the list to a tupil will work the same way as the for in loop
#players = ('Altuve', 'Bregman', 'Correa', 'Gattis')


#working with dictionaries
#looping with each data structure
#we need to grab the key and the value
players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis'
}
#pass in two variables o our block variable possession is going
#  to be equal to the key which is second base and then player is going to be equal 
# to the value which in this case is Altuve. The next time players positions going to be third
#  base and player is going to be Bragman and all the way down the list 
for position, player in players.items():
    print('Position', position)
    print('Player Name', player)
"""
Position 2b
Player Name Altuve
Position 3b
Player Name Bregman
Position ss
Player Name Correa
Position dh
Player Name Gattis
"""