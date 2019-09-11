import random

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
            break
        print ('You have ' + str(total_guesses) + ' guesses left.')

        guess = input('Please guess a letter: ')

        if guess in secret_word:
            if guess in letters_guessed:
                print ("You have guessed that letter already, please try something else: " + get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(guess)
                print ('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
                
        else:
            if guess in letters_guessed:
                print ("You have guessed that letter already, please try something else: " + get_guessed_word(secret_word, letters_guessed))               
            else:
                letters_guessed.append(guess)
                total_guesses-= 1
                print ('Oops! That letter is not in the word: ' + get_guessed_word(secret_word, letters_guessed))
               

    if correct_guess == True:
        print("\n")
        return 'goodjob You have correcely guessed the word! ' + secret_word
    elif total_guesses == 0:
        print("\n")
        print ('Sorry, you lost. The word was ' + secret_word)


secret_word = load_word()
spaceman(secret_word)