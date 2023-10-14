"""
1. 
Create a function filter_integer_data, which takes a list as a parameter 
and checks each element whether it is of type integer. The return value of the list is a list of 
integer values.

result = filter_integer_data(["a", 3, 1, 3.3])
Result: [3, 1]

"""

a = ["a", 3, 1, 3.3]

def filter_integer_data(list):
    """Remove from a sequence all elements that are not an integer."""
    filtered = []
    for i in list:
        if isinstance(i, int):
            filtered.append(i)
        continue
    return filtered 


print(filter_integer_data(a))

# with list comprehension
c = [i for i in a if isinstance(i, int)]
print(c)



"""
2.
Create a function check_values which gets a list of float values and a
tuple. The function checks if all elements
are in the closed interval [a, b]. The return value is a boolean.

check_values(values, interval):
    ...

result = check_values([2, 2.2, 4, 2.3, 0.1], (1, 5.3))
Result: False

"""

floats = ([2, 2.2, 4, 2.3, 0.1], (1, 5.3))

def check_values(values, interval):
    """Check if values are present in the closed interval."""
    for value in values:
        if value < interval[0] or value > interval[1]:
           return False
    return True


def check_values_2(values, interval):
    """Check if values are present in the closed interval."""
    a, b = interval
    return all([a <= value <= b for value in values])


print(check_values([2, 2.2, 4, 2.3, 0.1], (1, 5.3)))
