"""
Implement all functions in only one line of code!
They should contain a single return statement.
If you think of several implementations, do them all.
No need to validate user input anywhere.
"""
import functools
from string import ascii_letters
from collections import Counter


def sum_digits(num):
    """
    Computes the sum of digits of an integer.
    """
    return sum([int(i) for i in str(num)])


print(sum_digits(123))


def is_palindrome(seq):
    """
    Checks whether a given sequence is a palindrome.
    (without changing the original sequence)

    Hints:
    - there are 2 easy ways:
        - one using builtin functions
        - another using a knife
    """
    return "".join(list(reversed(seq))) == seq
    # return seq[::-1] == seq


print(is_palindrome("abcba"))


def is_gmail(string: str):
    """
    Checks whether a string is a Gmail email address.

    For our purposes, a valid address looks like "abcd@gmail.com".
    It must be a string of alphabetic letters (no dots) followed by '@gmail.com'.
    """
    return string.endswith("gmail.com")


def union(items: list, more_items: list):
    """
    Unites 2 lists/tuples into a list/tuple that contains all their elements without duplication.
    The return type must be that of the first argument `items`.
    """
    return items + [i for i in more_items if i not in items]


print(union([1, 2, 3, 4], [1, 2, 2, 11]))


# This is not a one-liner challenge, but should be 4 lines max
def distribution(items: list):
    """
    Finds how many times each item appears in a sequence of items.
    """
    # dist = {}
    # for item in items:
    #     dist[item] = items.count(item)
    # return dist
    return {i: items.count(i) for i in items}


# remember us? :)
formula1Champions = [
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Alonso",
    "Alonso",
    "Räikkönen",
    "Hamilton",
    "Button",
    "Vettel",
    "Vettel",
    "Vettel",
    "Vettel",
    "Hamilton",
    "Hamilton",
    "Rosberg",
    "Hamilton",
    "Hamilton",
    "Hamilton",
    "Hamilton"
]

print("distribution", distribution(formula1Champions))


def all_time_champion(champions: list):
    """
    Finds the person has the most wins.

    Hints:
    - distribution
    - max
    - lambda
    """
    return max(distribution(champions).items(), key=lambda x: x[1])[0]


print("all time champion", all_time_champion(formula1Champions))


def dictify(keys, values):
    """
    Creates a dict mapping the given keys to the given values.
    """
    return {keys[i]: values[i] for i in range(len(keys))}


print(dictify([1, 2, 3], ["s", "23", 55]))


def is_prime(num):
    """
    Checks whether a number is prime.

    Hints:
    - I can do this any day, and all day long!
    """
    return [i for i in range(1, num) if num % i == 0 and (i != 1 or i == num)] == []


print("prime", is_prime(12))


def caesar_encrypt(plain, key):
    """
    Encrypts a string using caesar cipher, with the given key as the offset.

    Hints:
    - from string import ascii_letters
    - https://www.youtube.com/watch?v=IjcX3MVSdyA
    """
    return "".join([ascii_letters[ascii_letters.index(i) - key] for i in plain])


print(caesar_encrypt("bcd", 1))


def all_time_champion2(champions):
    """
    Your previous code is cool, but now make it shorter!

    Hints:
    - from
    - collections
    - import
    - Counter
    """
    return Counter(champions).most_common(1)


def factorial(num):
    """
    Computes the factorial of a number (1 * 2 * 3 * ... * num).

    Hints:
    - def factorial(num):
          '''
          Computes the factorial of a number (1 * 2 * 3 * ... * num).

          Hints:
          - ...
          '''
          pass
    """
    # solution 1:
    # return functools.reduce(lambda a, b: a * b, [i + 1 for i in range(num)])

    if num == 1:
        return 1
    return num * factorial(num - 1)


def compose(*funcs):
    """
    Composes all given functions.
    compose(f, g, h)(x) == f(g(h(x)))

    Hints:
    - from functools import reduce
    """
    return functools.reduce(lambda a, b: b(a), funcs)


def x(x):
    print(x)


def y(y):
    return y


def z(z):
    return z

t = compose(x, y, z)
print(t)