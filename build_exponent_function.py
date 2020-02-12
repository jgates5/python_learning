from functools import reduce

"""
manual_exponent(2, 3)
#> 8

manual_exponent(10,2)
#>100
"""

def manual_exponent(num, exp):
    computed_list = [num] * exp
    return(reduce(lambda total, element: total * element, computed_list))

"""Computed_list = [3] * 2
[3, 3]
#counter = exp -1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total
"""
print(manual_exponent(2, 3))
print(manual_exponent(10,2))


lambda function that does not have -name see how it works
def some_function(total, element):
    return * element

[2, 2, 2]
some_function(2, 2)
some_function(4, 2)
comes to be 8
    reduce is a list its going to call some function
    start at a total of 0 by default and going to take the first element of 1