"""create a set of cubed numbers which means 
I want to multiply each one of the items in this range
and I want to cube them. So I want to add an exponent of 3 so that it will 
return back a list where each one of the elements has been cubed
"""
#num_list = range(1, 11)
#cubed_nums = []

#for num in num_list:
    #cubed_nums.append(num ** 3)

#list comprehension (x) can be called anything
#cubed_nums = [x ** 3 for x in num_list]
#cubed_nums = [num ** 3 for num in num_list]
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#print(cubed_nums)
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#capture a list that is an even number
#num_list = range(1, 11)
"""
even_numbers = []

for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]
print(list(num_list))
print(even_numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10]
"""

#using conditionals
"""num_list = range(1, 11)
even_numbers = [num for num in num_list if num % 2 == 0]

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10]
print(list(num_list))
print(even_numbers)"""

"""num_list = range(1, 100)

odd_numbers = []

for num in num_list:
    if num % 3 == 0:
        odd_numbers.append(num)

print(odd_numbers)"""

"""
num_list = range(1, 100)

odd_numbers = [num for num in num_list if num % 3 == 0]

print(odd_numbers)"""