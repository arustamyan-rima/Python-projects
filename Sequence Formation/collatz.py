"""
The problem involves sequences of numbers constructed according to a simple law of formation:

    Start with any natural number n > 0.
    If n is even, take next n / 2 .
    If n is odd, take 3 * n + 1 next.
    Repeat the procedure with the obtained number.

For example, for the starting number n = 19, you get the sequence:
19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1,

For example, the function shall terminate (exit) when n == 1.
The function shall not be implemented recursively.
"""


def fn(n):
    if n > 0 and n - int(n) == 0:
        L = [n]
        while L[-1] != 1:
            if L[-1] % 2 == 0:
                L.append(int(L[-1] / 2))
            else:
                L.append(3 * L[-1] + 1)
        return L 
    else:
        print(False)


print(fn(19))

# alternative

def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

        print(number)


print('Enter the number to Collatz:')
collatz(int(input(":")))