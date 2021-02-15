import os
from math import *
from string import *
from itertools import *

# Midterm Problem 3

# def Square(x):
#     return SquareHelper(abs(x), abs(x))
#
# def SquareHelper(n, x):
#     if n == 0:
#         return 0
#     return SquareHelper(n-1, x) + x


'''
Question:
Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.

For example:
    count7(717) -> 2
    count7(1237123) -> 1
    count7(8989) -> 0
This function has to be recursive; you may not use loops! This function takes in one integer and returns one integer.
'''

'''
Solution:
def count7(N):
    # N: a non-negative integer
    # Your code here
    if N%10 == 7:
        return count7(N//10)+1
    elif N == 0:
        return 0
    else:
        return count7(N//10)
'''

# Midterm Problem 4

'''
Question:
Write a Python function that returns the sum of the pairwise products of listA and listB. 
You should assume that listA and listB have the same length and are two lists of integer numbers.
For example, if listA = [1, 2, 3] and listB = [4, 5, 6], 
the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32
'''

'''
Solution:
This function takes in two lists of numbers and returns a number.
def dotProduct(listA, listB):
	sum = 0
	for i in range(len(listA)):
		sum += listA[i]*listB[i]
	return sum
'''

# Midterm Problem 5

'''
Question:
Write a Python function that returns a list of keys in aDict with the value target. 
The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers.
(If aDict does not contain the value target, you should return an empty list.)
'''

'''
Solution:
This function takes in a dictionary and an integer and returns a list.
def keysWithValue(aDict, target):
	values = aDict.values()
	newlist = []
	for key in aDict:
		if aDict[key] == target:
			newlist.append(key)
	return newlist
'''

# Midterm Problem 6

'''
Question:
Write a function called gcd that calculates the greatest common divisor of two positive integers.
The gcd of two or more integers, when at least one of them is not zero,
is the largest positive integer that divides the numbers without a remainder.
One way is recursively, where the greatest common denominator of a and b can be calculated as gcd(a, b) = gcd(b, a mod b).
    For example, the greatest common divisor (gcd) between a = 20 and b = 12 is:
    gcd(20,12) is the same as gcd(12, 20 mod 12) = gcd(12,8)
    gcd(12,8) is the same as gcd(8, 12 mod 8) = gcd(8,4)
    gcd(8,4) is the same as gcd(4, 8 mod 4) = gcd(4,0)
    The gcd is found (and the gcd is equal to a) when we reach 0 for b
'''

'''
Solution:
def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b,a%b)
'''

# Midterm Problem 7

'''
Question:
Write a Python function called satisfiesF that has the specification below.
Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
For your own testing of satisfiesF, for example, see the following test function f and test code:
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
Should print:
    2
    ['a', 'a']
'''

'''
Solution:
def satisfiesF(L):
	L[:] = [string for string in L if f(string) == 1]
	return len(L)
run_satisfiesF(L, satisfiesF)
'''


