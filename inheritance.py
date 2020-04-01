class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User):
    #find out active user on the site
    def active_user(self):
        return '500'

tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany',
'Hudgens')

Christine = User('Kristine@devcamp.com', 'Kristine',
'Hudgens')

print(tiffany.active_user())
print(tiffany.greeting())