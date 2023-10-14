
"""
1. count vowels
Write a function count_vocals() which expects a string as parameter,
and counts all vowels in this string. The return value of the function is the
number of vowels (int).

Example:
number_of_vocals = count_vocals("teleport").
// 3
"""

def count_vocals(string):
    """Count the number of german vowels in a word."""
    vocals = "aeiouüöä"
    return len([char for char in string.lower() if char in vocals])

number_of_vocals = count_vocals("teleport")
print (number_of_vocals)

"""
2. filter list
Write a function filter_input(), which takes a list A and
and checks if these values are allowed by another list B with allowed values.
The return value of the function is a list of values that has been checked using B.

Example
input_filtered = filter_input([1, 3, 4, 5, 3], [3, 4])
print(input_filtered)
// [3, 4, 3]

input_filtered = filter_input([1, 3, 4, 5, 3], [])
print(input_filtered)
// []

input_filtered = filter_input(["gold", "yellow", "yellow", "red", "yellow"], ["yellow", "red"])
// ["yellow", "yellow", "yellow", "red"]
"""
A = [1, 3, 4, 5, 3]
B = [3, 4]


def filter_input(list1, list2): 
    """Filter Function."""
    return [values for values in list1 if values in list2] 

print(filter_input(A, B))


"""
3. reverse
Write a function reverse_cutter(), that takes a string, transforms it to lowercase,
truncates the first and last index and returns the result reversed.
An input less than or equal to two returns an empty string.
 Example:
reversed = reverse_cutter("Petersburg")
// rubsrete
"""

def reverse_cutter(thestring):
    return thestring[::-1][1:-1].lower()

print(reverse_cutter('THEstring'))

"""
4. max
Implement the function max, which should return the largest value from a given list
of integer values. The function should return None if an empty list was passed.  

Example:
values = [3, 2, 4]
x_max = max(values)
// 4

values = []
x_max = max(values)
// None
"""

def max(yourlist):
    """Get the max value of iterable or None, if empty."""
    import math
    m = - math.inf
    if len(yourlist) == 0:
        return None
    for x in yourlist:
        if x >= m:
            m = x
    return m 

# alternative
def max_value(values):
    """Get the max value of iterable or None, if empty."""
    return None if not values else sorted(values, reverse=True)[0]

"""
5. median
Implement the function median(), which takes a list of integer values
and calculates the median. 

Example:
values = [1, 2, 4, 8, 2, 19]
x_median = median(values)
// 3.0
"""

def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[int(n/2)] + numbers[int((n + 2)/2)]) / 2
    else: 
        median = numbers[int((n + 1)/2)]
    return median 

values = [1, 2, 4, 8, 2]
print(median(values))
