# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

# Define global constants
WORDLIST_FILENAME = "words.txt"
ALREADY_GUESSED = -1
NOT_A_LETTER = -2
WRONG_GUESS = -3

def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: 
        string, the word the user is guessing; 
        assumes all letters are lowercase.
    letters_guessed: 
        list (of letters), which letters have been guessed so far;
        assumes that all letters are lowercase.
    returns: 
        boolean
        True if all the letters of secret_word are in letters_guessed;
        False otherwise.
    '''
    guessed = True  # Init as true and set to fales if not all letters
                    # in secret word are guessed.
                    
    #Loop through secret_word and see if any letters are not in letters_guessed
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed = False
            break
    
    return guessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: 
        string, the word the user is guessing
    letters_guessed: 
        list (of letters), which have been guessed so far
    returns: 
        string, comprised of letters, underscores (_), and spaces representing
        which letters in secret_word have been guessed so far.
    '''
    
    guess=""
    
    #Loop through secret_word and check if letter guessed
    #if Guessed add letter to guess
    for letter in secret_word:
        if letter in letters_guessed:
            guess += letter
        else:
            guess += ' _'
            
    return guess
    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which have been guessed so far
    
    returns: string (of letters), comprised of letters that represents which 
    letters have not yet been guessed.
    '''
    import string
    
    not_guessed_yet = ''
    
    #Loop through lower case letters and put letters not in letters_guessed
    #in not_guessed_yet
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            not_guessed_yet += letter
        else:
            not_guessed_yet += ' '
    
    return not_guessed_yet
    
def get_guess(letters_guessed, warnings_and_guesses_left):
    '''
    get_guess displays the number of guesses remaining and 
    the available letters and then asks the user for a guess.  
    If the guess is valid (i.e. not guessed before, and a letter.) 
    Then get_guess returns the guess as lower case.  
    If the guess is not valid it returns an error number.
     
    letters_guessed:
        list;
        List of the letters already guessed.
         
    warnings_and_guesses_left:
        tuple length 2
        [0] = number of warnings left;
            >=0 number of warnings remaining no guess has been taken away
            ==-1 no warnings guess has been taken away
        [1] = number of guesses left in the game.
         
    return:
        The guess in lower case for a valid guess;
        NOT_A_LETTER if the guess is not a letter;
        ALREADY_GUESSED if the letter was already guessed.
    '''

    # Seperator String and guesses left in game and availble letters for guess
    print("You have", warnings_and_guesses_left[1], "guesses left.")
    print("Available letters:", get_available_letters(letters_guessed))
    print("Available letters:", "ABC")
    
    # Get guess from user and put in lower case
    guess = input("Please guess a letter: ")
    
    # Check if valid guess
    if guess not in string.ascii_letters:
        guess = NOT_A_LETTER
    elif guess in letters_guessed:
        guess = ALREADY_GUESSED
    else:
        guess = guess.lower()

    return guess

def update_warnings_and_guesses_left(guess,
                                     secret_word,
                                     warnings_and_guesses_left):
    '''
    update_warnings_and_guesses_left looks at guess and secret_word to update
    the warnings and guesses left:  
        
        If guess is in secret_word it returns warnings_and_guesses_left 
            unchanged;
            
        If guess is a consonent and not in secret_word:
            Decrement warnings_and_guesses_left[1] by 1;
            
        If guess is a vowel and not in secret_word:
            Decrement warnings_and_guesses_left[1] by 2;    

        If guess is NOT_A_LETTER or ALREADY_GUESSED it changes 
            warnings_and_guesses_left as follows:
                warnings > 0:
                    decrement warnings_and_guesses_left[0] by 1 
                    no change to warnings_and_guesses_left[1] 
                warnings = 0:
                    decrement warnings_and_guesses_left[0] by 1
                    decrement warnings_and_guesses_left[1] by 1
                warnings = -1:
                    no change to warnings_and_guesses_left[0] 
                    decrement warnings_and_guesses_left[1] by 1
                    
    guess:
        lower case letter or error number;
        lower case letter;
            Guess was vaild;
        ALREADY_GUESSED;
            guess was already guessed
        NOT_A_LETTER;
            guess is not a letter
            
    secret_word:
        string;
        a string containing the word the user is trying to guess
        
    warnings_and_guesses_left:
        tuple length 2
        [0] = number of warnings left;
            >=0 number of warnings remaining no guess has been taken away
            ==-1 no warnings guess has been taken away
        [1] = number of guesses left in the game.
         
    return:
        The updated warnings_and_guesses_left
    '''    


    if guess == NOT_A_LETTER or guess == ALREADY_GUESSED:
        # Invalid input update warnings and guesses as described above
        if warnings_and_guesses_left[0] > 0:
            warnings = warnings_and_guesses_left[0] - 1
            guesses = warnings_and_guesses_left[1]
            
        elif warnings_and_guesses_left[0] == 0:
            warnings =  -1
            guesses = warnings_and_guesses_left[1] - 1
            
        elif warnings_and_guesses_left[0] == -1:
            warnings =  -1
            guesses = warnings_and_guesses_left[1] - 1
        else:
            #invalid number of warnings
            print("invalid number of warnings in ",
                  "update_warnings_and_guesses()")

    elif guess.isalpha() and guess not in secret_word:
        # Bad Guess updated guesses as described above
        if guess in 'aeiou':
            #Vowel, subtract 2 guesses, no change to warnings
            warnings = warnings_and_guesses_left[0]
            guesses = warnings_and_guesses_left[1] - 2 
        
        else:
            #Consonent, subtract 1 guess, no change to warnings
            warnings = warnings_and_guesses_left[0]
            guesses = warnings_and_guesses_left[1] - 1  

    else:
    # Good Guess don't change anything
        warnings = warnings_and_guesses_left[0]
        guesses = warnings_and_guesses_left[1] 
    
    return (warnings, guesses)

def show_guess_results(guess, 
                        secret_word, 
                        letters_guessed, 
                        warnings_and_guesses_left):
    '''
    show_guess_results looks at guess and secret_word to display results
    of the guess:  
             
    guess:
        lower case letter or error number;
        lower case letter;
            Guess was vaild;
        ALREADY_GUESSED;
            guess was already guessed
        NOT_A_LETTER;
            guess is not a letter
            
    secret_word:
        string;
        a string containing the word the user is trying to guess
        
    letters_guessed:
        list;
        List of the letters already guessed.

    warnings_and_guesses_left:
        tuple length 2
        [0] = number of warnings left;
            >=0 number of warnings remaining no guess has been taken away
            ==-1 no warnings guess has been taken away
        [1] = number of guesses left in the game.
         
    return:
        None
    '''
    # Build message to display
    if guess == ALREADY_GUESSED:
        if warnings_and_guesses_left[0] == -1:
            warning_count = "no"
        else:
            warning_count = str(warnings_and_guesses_left[0])
        message = (
                "Oops! You've already guessed that letter. You have " +
                  warning_count +
                  " warnings left:\n" +
                  get_guessed_word(secret_word, letters_guessed)
                  )
        
    elif guess == NOT_A_LETTER:
        if warnings_and_guesses_left[0] == -1:
            warning_count = "no"
        else:
            warning_count = str (warnings_and_guesses_left[0])
        message = (
                  "Oops! That is not a valid letter. You have" +
                  warning_count +
                  " warnings left: " +
                  get_guessed_word(secret_word, letters_guessed)
                  )
                          
    elif guess not in secret_word:
        message = (
                  "Oops! That letter is not in my word: " +
                  get_guessed_word(secret_word, letters_guessed)
                  )
    else:
        message = ("Good guess: " + 
                  get_guessed_word(secret_word, letters_guessed)
                  )
        
                              
                          
    #Print user message
    print(message)                      
        
    # Print seperator between turns
    print("------------")  
    
    return None

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Define and Initialize Variables used to play the game.
    
        
    # Get word to be guessed --- For Debug use 'apple' 
    #secret_word = choose_word(wordlist)
    secret_word = "apple"
    
    # Start with no letters guessed, 3 warnings, 6 guesses and won_game False
    letters_guessed = []
    warnings_and_guesses_left = (3,6)
    won_game = False
    
    
    # Print Welcome Screen
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", 
          len(secret_word), 
          "letters long.")
    print("You have", warnings_and_guesses_left[0], "warnings left.")
    print("------------")
    
    ########## Main Game Loop #################################################
    while warnings_and_guesses_left[1] > 0:
        
        # Get Guess from user
        guess = get_guess(letters_guessed, warnings_and_guesses_left)
        if guess != ALREADY_GUESSED and guess != NOT_A_LETTER:
            #valid guess add letter to letters_guessed
            letters_guessed.append(guess)
              
        # Update warnings and guesses left based on guess
        warnings_and_guesses_left = update_warnings_and_guesses_left(
                                          guess,
                                          secret_word,
                                          warnings_and_guesses_left)
        
        # Display results of guess to user
        show_guess_results(guess, 
                           secret_word, 
                           letters_guessed, 
                           warnings_and_guesses_left)
        
        # Check to see if user won the game
        if is_word_guessed(secret_word, letters_guessed):
            # WON GAME !!
            won_game = True
            break
        
    ############# End of Main Game Loop #######################################
            
            
    print("won_game = ", won_game)
        

            
            
  

   

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the 
      user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
    secret_word = 'apple'
    hangman(secret_word)
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
