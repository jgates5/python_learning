"""
And so if I create a variable here called role and imagine 
that you have a user logged in who's an admin from here what 
we want to do is we want to check to see if role is set to admin. 
So when that user logs in and we check to see their credentials if it 
says that their role is admin then we want them to access the dashboard.
And if not, say they're a guest user then we do not
""""""
role = 'admin'

#creating a variable storing the ouput ternary operator
# you can access this if the role is set to admin. If not then you cannot access it.
auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)
#can access
"""

role = 'guest'
 
if role == 'admin':
    auth = 'can access'
else:
    auth = 'cannot access'
print(auth)


