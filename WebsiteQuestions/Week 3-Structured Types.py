import os
import string


# Hangman Game
# WORDLIST_FILENAME = "words.txt"
'''
Helper code
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
'''

# Load the list of words into the variable wordlist so that it can be accessed from anywhere in the program
# wordlist = loadWords()


# Questions and Solutions for the questions on the course website.

# Week 3 Problem 1

'''
Question:
Is the Word Guessed
First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, 
lettersGuessed. This function returns a boolean - True if secretWord has been guessed 
(ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))
    False
'''
'''
Solution:
# For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

def isWordGuessed(secretWord, lettersGuessed):
    new = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            new += letter
            if new == secretWord:
                return True
        else:
            return False
'''

# Week 3 Problem 2

'''
Question:
Getting the User's Guess
implement the function getGuessedWord that takes in two parameters - a string, secretWord, 
and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, 
based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!
Example Usage:

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
    '_ pp_ e'
    
When inserting underscores into your string, it's a good idea to add at least a space after each one,
so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ).
This is called usability - it's very important, when programming, to consider the usability of your program. 
If users find your program difficult to understand or operate, they won't use it!
'''

'''
Solution:
For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
def getGuessedWord(secretWord, lettersGuessed):
    # secretWord: string, the word the user is guessing
    # lettersGuessed: list, what letters have been guessed so far
    # returns: string, comprised of letters and underscores that represents
    # what letters in secretWord have been guessed so far.
    
    new = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            new += letter
        else:
            new += "_"
    return new
'''

# Week 3 Problem 3

'''
Question:
Printing Out all Available Letters
implement the function getAvailableLetters that takes in one parameter - a list of letters,
lettersGuessed. This function returns a string that is comprised of lowercase English letters - 
all lowercase English letters that are not in lettersGuessed.
Example Usage:
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
    abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as in the example above.
'''

'''
Solution:
def getAvailableLetters(lettersGuessed):
    # lettersGuessed: list, what letters have been guessed so far
    # returns: string, comprised of letters that represents what letters have not
    # yet been guessed.
    newstring = ''
    for char in string.ascii_lowercase:
        if char in lettersGuessed:
            continue
        newstring += char
    return newstring
'''

# Week 3 Problem 4

'''
Question:
The Game
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. 
This starts up an interactive game of Hangman between the user and the computer. 
Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
- There are four important pieces of information you may wish to store:
secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses a letter,
the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, 
you should print a message telling them they've already guessed that - so try again!).
'''

'''
Solution
def hangman(secretWord):
    
    # secretWord: string, the secret word to guess.
    # 
    # Starts up an interactive game of Hangman.
    # 
    # * At the start of the game, let the user know how many 
    #   letters the secretWord contains.
    # 
    # * Ask the user to supply one guess (i.e. letter) per round.
    # 
    # * The user should receive feedback immediately after each guess 
    #   about whether their guess appears in the computers word.
    # 
    # * After each round, you should also display to the user the 
    #   partially guessed word so far, as well as letters that the 
    #   user has not yet guessed.
    # 
    # Follows the other limitations detailed in the problem write-up.

def hangman(secretWord):
    mistakesMade = 8
    lettersGuessed = []

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    print("-----------")
    print("You have {} guesses left.".format(mistakesMade))
    print("Available letters:"+getAvailableLetters(lettersGuessed))
    while mistakesMade >= 1 and isWordGuessed(secretWord, lettersGuessed) != 1:
        userguess = input("Please guess a letter:")
        if len(userguess) != 1:
            userguess = input("Please guess a letter:")
        elif userguess in lettersGuessed:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord,lettersGuessed))
            print("-----------")
            print("You have {} guesses left.".format(mistakesMade))
            print("Available letters:" + getAvailableLetters(lettersGuessed))
        elif userguess in secretWord:
            lettersGuessed += userguess
            if isWordGuessed(secretWord,lettersGuessed) == 1:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                print("Congratulations, you won!")
                break
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            print("You have {} guesses left.".format(mistakesMade))
            print("Available letters:" + getAvailableLetters(lettersGuessed))
        elif userguess not in secretWord:
            lettersGuessed += userguess
            mistakesMade -= 1
            print("Oops! That letter is not in my word:" + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            if mistakesMade > 0:
                print("You have {} guesses left.".format(mistakesMade))
            else:
                break
            print("Available letters:" + getAvailableLetters(lettersGuessed))
    if mistakesMade < 1:
        print("Sorry, you ran out of guesses. The word was "+secretWord)
'''

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
