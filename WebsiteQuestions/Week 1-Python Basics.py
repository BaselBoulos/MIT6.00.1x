import os

# Questions and Solutions for the questions on the course website.

# Week 1 Problem 1
'''
Question:
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
    Number of vowels: 5
'''

'''
Solution
count = 0
vowels = ['a' , 'e' , 'i' ,'o' , 'u']
for char in s:
    if char in vowels:
        count += 1
print("Number of vowels:" + str(count))
'''

# Week 1 Problem 2
'''
Question:
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
    Number of times bob occurs is: 2
'''

'''
Solution
counter = 0
for i in range(0,len(s)-2):
    if s[i:i+3]=='bob':
        counter += 1
        i += 1
print(counter)
'''

# Week 1 Problem 3
'''
Question:
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
    Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
    Longest substring in alphabetical order is: abc
'''

'''
lstring = ''
res = ''
for i in range(len(s)):
    lstring += s[i]
    if len(lstring) > len(res):
        res = lstring
    if i > len(s)-2:
        break
    if s[i] > s[i+1]:
        lstring = ''
print("Longest substring in alphabetical order is: {}".format(res))
'''