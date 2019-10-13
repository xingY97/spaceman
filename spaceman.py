import random
import os
def load_word():

    f = open('words.txt', "r")
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    # TODO: Loop through the letters in the secret_word and check if a letter is not in letters_guessed
   
    letters = ""
    if letters == secret_word:
        return True
    else:
        return False
    
def get_guessed_word(secret_word, letters_guessed):
    # TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guess = ""
    for letters in secret_word:
        if letters in letters_guessed:
            guess += letters
        else:
            guess += " _ "
    return guess

def is_guess_in_word(guess,secret_word):
    # TODO: Check if the letter guess is in the secret word
    return (guess in secret_word)

def playagain(player):
    while True:
        if player.isalpha():
            if player == 'y':
                spaceman(load_word())
            elif player == 'n':
                return False
            else:
                print('Please follow firection!')


def spaceman(secret_word):
    #tell user about spaceman game
    print("Welcome to Spaceman!\nThe secret word contains: " + str(len(secret_word)) + " letters")
    correct_guess = False
    guess = ""
    letters_guessed =[]
    guess_count = 0
    total_guesses = 7

    while total_guesses> 0 and total_guesses<= 7 and correct_guess is False:
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            wordGuessed = True
            
        print ('You have ' + str(total_guesses) + ' guesses left.')

        guess = input('Please guess a letter: ')
        #check if user has guessed the word
        if guess in secret_word:
            if guess in letters_guessed:
                print ("You have guessed that letter already, please try something else: " + get_guessed_word(secret_word, letters_guessed))
                print ("\n")
                
            else:
                letters_guessed.append(guess)
                print ("You got one ! : " + get_guessed_word(secret_word, letters_guessed))
                print("\n")
                
        else:
            if guess in letters_guessed:#check if user have gussed the letter already
                print ("You have guessed that letter already, please try something else: " + get_guessed_word(secret_word, letters_guessed))
                print("\n")               
            else:
                letters_guessed.append(guess)
                total_guesses-= 1
                print ("Oops! That letter is not in the word: " + get_guessed_word(secret_word, letters_guessed))
                print("\n")
               

    if correct_guess == True:
        print("\n")
        return 'goodjob You have correcely guessed the word! ' + secret_word
    elif total_guesses == 0:
        print("\n")
        print ('Sorry, you lost. The word was ' + secret_word)



secret_word = load_word()
#spaceman(secret_word)

def test_is_word_guessed ():
    assert is_word_guessed ("ape",['a','p','p','l','e']) == False
    assert is_word_guessed("abs",['a','b','s']) == False
    
def test_is_guess_in_word():
    assert is_guess_in_word("apple",['apple']) == True
    assert is_guess_in_word("banana",['banana']) == True

def test_pay_again():
    assert playagain('n')==False


if __name__ == "__main__":
    test()
    test_is_word_guessed()
    test_get_guessed_word()
    test_is_guess_in_word()