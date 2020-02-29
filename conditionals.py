"""
age = 15
if age < 25: #<--everytime you see a colen you need to indent on the next line
    print(f"I'm sorry you need to be at least 25 years old")

else:
    print(f"You're good to go, {age} fits in the age to rent a car.")
"""
age = 50
if age < 25: #<--everytime you see a colen you need to indent on the next line
    print(f"I'm sorry you need to be at least 25 years old")
elif age > 100:
    print(f"I am sorry, {age} is too old to rent a car")
else:
    print(f"You're good to go, {age} fits in the age to rent a car.")
