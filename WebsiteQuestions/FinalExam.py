import os
import string

# Final Exam Problem 3

'''
Question:
Numbers in Mandarin follow 3 simple rules.

There are words for each of the digits from 0 to 10.
For numbers 11-19, the number is pronounced as "ten digit", so for example, 16 would be pronounced (using Mandarin) as "ten six".
For numbers between 20 and 99, the number is pronounced as “digit ten digit”, so for example, 37 would be pronounced 
(using Mandarin) as "three ten seven". If the digit is a zero, it is not included.
We want to write a procedure that converts an American number (between 0 and 99), written as a string, into the equivalent Mandarin.
    convert_to_mandarin('36') will return san shi liu
    convert_to_mandarin('20') will return er shi
    convert_to_mandarin('16') will return shi liu
'''

'''
Solution:
def convert_to_mandarin(us_num):
    """
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    """
    # FILL IN YOUR CODE HERE
    result = ""
    if int(us_num) < 0:
        return None
    elif int(us_num) <= 10:
        return trans[str(int(us_num))]
    elif int(us_num) >= 11 and int(us_num) <= 19 and int(us_num) // 10 == 1 and int(us_num) % 10 <= 9:
        return trans['10'] + ' ' + trans[str(int(us_num)%10)]

    elif int(us_num) > 19 and int(us_num) <= 99 and int(us_num)//10 > 1 and int(us_num)%10 <= 9:
        if int(us_num)%10 == 0:
            return trans[str(int(us_num) // 10)] + ' ' + trans['10']
        else:
            return trans[str(int(us_num)//10)] + ' ' + trans['10'] + ' ' + trans[str(int(us_num)%10)]
    else:
        return us_num
'''

# Final Exam Problem 4

'''
Question:
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here
'''

'''
Solution:
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # Your code here
    dec_count = 0
    inc_count = 0
    maxcount = 0
    result = 0
    for i in range(len(L) - 1): # iterate through all numbers
        if (L[i] <= L[i + 1]): # for ex if ( 10 <= 4 )
            dec_count += 1 # then decreasing is +1
            if dec_count > maxcount: 
                maxcount = dec_count
                result = i + 1
        else:
            dec_count = 0
        if (L[i] >= L[i + 1]):
            inc_count += 1
            if inc_count > maxcount:
                maxcount = inc_count
                result = i + 1
        else:
            inc_count = 0

    start = result - maxcount
    return sum(L[start:result + 1])

L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] # [3, 4, 5, 7, 7]

print(longest_run(L))
'''

# Final Exam Problem 5

'''
Question:
def uniqueValues(aDict):
    """
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    """
    # Your code here
'''

'''
Solution:
def uniqueValues(aDict):
    """
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    """
    # Your code here
    if len(aDict) == 0:
        return []
    elif len(aDict) >= 2:
        value_list = []
        key_list = []
        for value in aDict.values():
            value_list.append(value)
        for key,value in aDict.items():
            if value_list.count(value) == 1:
                key_list.append(key)
        return sorted(key_list)
'''

# Final Exam Problem 6

'''
Question:
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + self.say(stuff)

As written, this code leads to an infinite loop when using the Arrogant Professor class.

Change the definition of ArrogantProfessor so that the following behavior is achieved:
'''

'''
Solution:
class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self,stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self,stuff)
'''

# Final Exam Problem 7

'''
Question:
You are given the following superclass. Do not modify this.
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
Write a class that implements the specifications below. Do not override any methods of Container.

'''

'''
Solution:
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        try:
            del self.vals[e]
        except:
            return None


    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        if e in self.vals.keys():
            return True
        else:
            return False
'''