# Angus Dillon
# 23 - 03 - 2021
# Scrabble assessment

# Initiates variables for the program
successful_word = False
existing_word = False
word_score = 0
word_len = 0

file = open('englishwords.txt', 'r')
real_words = file.readlines()
file.close()

# Identifies the letters related to the scores, aswell as special characters to check for
one = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r']
two = ['d', 'g']
three = ['b', 'c', 'm', 'p']
four = ['f', 'h', 'v', 'w', 'y']
five = ['k']
eight = ['j', 'x']
ten = ['q', 'z']

def scrabble():
    print()
    print('Your word was', word)
    print('Your word was', word_len, 'characters long')
    print('The word', word, 'is worth', word_score, 'scrabble points.')
    exit()

while successful_word == False:
    # Gets the input from the user.
    word = input('Please input a word \n')

    # Checks each character in the input for numbers or spaces, and makes a boolean value True if it does occur.
    for character in word:
        if not character.isalpha():
            print('You entered an invalid word/characters/numbers etc...')
        else:
            word_len = len(word)
            if word_len == 7:
                word_score += 50
                successful_word = True
            elif word_len > 7:
                print('Your word was too long. Please try agian with a word less than 7 letters long')
            else:
                successful_word = True


# Makes the user input lowercase for syntax clarification.
word_lower = word.lower()
word_letters = list(word_lower)

# Checks to see if the word is a real word in the english dictionary
for line in real_words:
    if word in line:
        existing_word = True
    else:
        ()

# Checks each letter in the word and adds a set value to score to the word_score variable.
if existing_word == True:
    for letter in word_letters:
        if letter in one:
            word_score += 1
        elif letter in two:
            word_score += 2
        elif letter in three:
             word_score += 3
        elif letter in four:
            word_score += 4
        elif letter in five:
            word_score += 5
        elif letter in eight:
            word_score += 8
        elif letter in ten:
             word_score += 10
        else:
            print('There was an error. Your input may appear to contain special characters only')
            exit()
else:
    print('You did not enter a real word')
    exit()

# Prints the statistics of the inputed word.
scrabble()
