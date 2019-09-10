import random

def load_word():

    f = open('/Users/xin/makeSchool/spaceman/words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    
    return True

def get_guessed_word(secret_word, letters_guessed):

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guesses = ""
    for letter in list(secret_word):
        if letter in letters_guessed:
            guesses += letter
            print(letter)
        else:
            guesses += ' _ '
    return guesses

def is_guess_in_word(guess, secret_word):
    #TODO: check if the letter guess is in the secret word
    return (guess in secret_word)

def spaceman(secret_word):
    
    print("welcome to spaceman")
    print("The secret word has " + str(len(secret_word)) + " letters, goodluck!")
    correct_guess = False
    guess = ""
    letters_guessed = []
    guess_count = 0
    guess_limit = 7
    guesses_left = len(secret_word)
    unused_letters = list('abcdefghijklmnopqrstuvwxyz')
    while guesses_left > 0 and correct_guess is False:

        if get_guessed_word == secret_word:
            print("you got it right, the word was" + secret_word)
            
        print('you have ' + str(guess_limit) + ' guesses left.')
        break

        if guess in secret_word:
    

    










    




    
        
    
        

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)