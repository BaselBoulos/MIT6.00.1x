import os
import string
# The 6.00 Word Game

'''
Helper Code:
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList
def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

End of helper code
'''

# Questions and Solutions for the questions on the course website.
# Part A + B
'''
Introduction: on the website.
'''

# Week 4 Problem 1
'''
Question:
Word Scores
The function getWordScore should accept as input a string of lowercase letters (a word) 
and return the integer score for that word, using the game's scoring rules.
'''

'''
Solution:
def getWordScore(word, n):
    sum = 0
    for char in word:
        if char in SCRABBLE_LETTER_VALUES.keys():
            sum += SCRABBLE_LETTER_VALUES.get(char)
    sum *= len(word)
    if n == len(word):
        sum += 50
    return sum
'''

# Week 4 Problem 2

'''
Question:
Dealing with Hands
Removing letters from a hand
The player starts with a hand, a set of letters. As the player spells out words, letters from this set are used up.
For example, the player could start out with the following hand: a, q, l, m, u, i, l. 
The player could choose to spell the word quail . This would leave the following letters in the player's hand: l, m.
Your task is to implement the function updateHand, which takes in two inputs - a hand and a word (string). 
updateHand uses letters from the hand to spell the word, and then returns a copy of the hand, 
containing only the letters remaining. For example:
    hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    displayHand(hand) # Implemented for you
         a q l l m u i
    hand = updateHand(hand, 'quail') # You implement this function!
    hand
        {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    displayHand(hand)
        l m  
Implement the updateHand function. Make sure this function has no side effects:
i.e., it must not mutate the hand passed in. Before pasting your function definition here        
'''

'''
Solution:
def updateHand(hand, word):
    hand2 = hand.copy()
    for char in word:
        if char in hand:
            if hand2[char] > 0:
                hand2[char] -= 1

    return hand2
'''

# Week 4 Problem 3

'''
Question:
Valid Words
A valid word is in the word list; and it is composed entirely of letters from the current hand. 
Implement the isValidWord function.
'''

'''
Solution:
def isValidWord(word, hand, wordList):
    if word not in wordList:
        return False
    newdic = getFrequencyDict(word)
    for key in newdic:
        if key not in hand.keys():
            return False
        else:
            if newdic[key] > hand[key]:
                return False

    return True
'''

# Week 4 Problem 4

'''
We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. 
This function allows the user to play out a single hand. First, though,
you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.
'''

'''
Solution:
def calculateHandlen(hand):
    return sum(hand.values())
'''

# Week 4 Problem 5

'''
Question:
Playing a Hand
# Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.
there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function
'''

'''
Solution:
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
        # Keep track of the total score
    totalscore = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand):
        # Display the hand
        displayHand(hand)
        # Ask user for input
        userword = input("Enter word, or a " "." " to indicate that you are finished: ")
        # If the input is a single period:
        if userword == ".":
            # End the game (break out of the loop)
            print("Good bye! Total score: " + str(totalscore) + " points.")
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(userword,hand,wordList):
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please Try again.:\n")
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totalscore += getWordScore(userword,n)
                print(userword +" earned " + str(getWordScore(userword,n)) + " points." + " Total: " + str(totalscore)+"\n")
                # Update the hand
                hand = updateHand(hand, userword)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    return "run out of letters. Total score: "+str(totalscore)+" points."
'''

# Week 4 Problem 6

'''
Question:
Playing a Game
A game consists of playing multiple hands. We need to implement one final function to complete our word-game program.
'''

'''

Solution:
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    n = HAND_SIZE
    hand = {}
    while True:
         userinput = input("Enter n to deal a new hand, r to replay the last hand,or e to end game: ")
         if userinput == "r":
             if not hand:
                 print('You have not played a hand yet. Please play a new hand first!')
             else:
                 playHand(hand, wordList, n)
         elif userinput == "n":
             hand = dealHand(n)
             playHand(hand,wordList,n)
         elif userinput == "e":
             break
         else:
             print("Invalid Command")
'''

# Part B Of Week 4
# Computer Choosing a Word and Playing a Hand
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord


#
# Computer plays a hand
'''
def compPlayHand(hand, wordList, n):

    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0):
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)):
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')
'''

# Week 4 Problem 7

'''
Question:
Now that your computer can choose a word, you need to give the computer the option to play. 
Write the code that re-implements the playGame function. 
You will modify the function to behave as described below in the function's comments. 
As before, you should use the HAND_SIZE constant to determine the number of cards in a hand. 
Be sure to try out different values for HAND_SIZE with your program.
'''

'''
Solution:
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO...
    while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            while True:
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif play_mode == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')            
        elif user_input == 'r':
            try:
                hand
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif play_mode == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print('Invalid command.')
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        else:
            print('Invalid command.')
'''

# if __name__ == '__main__':
#     wordList = loadWords()
#     playGame(wordList)