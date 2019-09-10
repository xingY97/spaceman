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
def play_again():
    print("Do you want to play again?(yes or no)")
    return input().lower().startswith('y')
def valid_input():
    while True:
        guess = input('Please guess a letter: ').lower()
        if guess.isalpha():
            if len(guess) > 1:
                print('invalid input: ' + guess)
                continue
            else:
                return guess
                break
        else:
            print('Not a valid input: ' + guess)
            continue
        

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
            correct_guess = False
            guess_limit -= 1
        print('you have ' + str(guess_limit) + ' guesses left.')
        break

        if guess in secret_word:
            if guess in unused_letters:
                print("good guess " + is_guess_in_word)
                print('___')
            else:
                 letters_guessed.append(guess)
            print("nice, " + get_guessed_word)
        else:
            if guess in secret_word:
                print("you have already tried that letter," + get_guessed_word)
            else:
                letters_guessed.append(guess)
                guesses_left -= 1
                print("that letter is not in the word: " + get_guessed_word)
                    
    

    










    




    
        
    
        

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)