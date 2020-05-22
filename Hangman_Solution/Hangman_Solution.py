import json
import random

# A learning exercise i Python
# Global variables
filename = 'resources/random_words.json'
SIZE = 0
word_list = None

used_letters = []
letter_not_found = "_"
next_letter = ""
str_to_print = ""
hangman_max_tries = 6
hangman_tries_left = 6
prompt_message = "Guess a letter:"
quit_message = "QUIT"
hangman = []
correct_guesses=[]


def construct_dictionary():
    with open(filename) as f:
       data = json.load(f)
       word_list = data["data"]
       return word_list

#Init hangman
def init_hangman():
    
    hangman_try_0 = [["__"], ["  |"]] 
    hangman_try_1 = [["__"], ["  |"],["  0"]]
    hangman_try_2 = [["__"], ["  |"],["  0"],[" | |"]]
    hangman_try_3 = [["__"], ["  |"],["  0"],["/| |"]]
    hangman_try_4 = [["__"], ["  |"],["  0"],["/| |\\"]]
    hangman_try_5 = [["__"], ["  |"],["  0"],["/| |\\"], [" /"]]
    hangman_try_6 = [["__"], ["  |"],["  0"], ["/| |\\"],[" / \\"]]
    hangman.append(hangman_try_0)
    hangman.append(hangman_try_1)
    hangman.append(hangman_try_2)
    hangman.append(hangman_try_3)
    hangman.append(hangman_try_4)
    hangman.append(hangman_try_5)
    hangman.append(hangman_try_6)

def print_hangman(tries_left):
   line_to_print = ""
   try_to_print = hangman[tries_left]
   next_line = ""
   for line in try_to_print:
       next_line = ""
       for char in line:
           next_line += char
       print(next_line)
      
       
   


# Choose a word randomly from a dictionary
def select_new_word(word_list, size):
    random_int = random.randint(0, size-1)
    random_word = word_list[random_int]
    return random_word

#Print a word using already guessed letters and blanks
def print_word_with_blanks(random_word , used_letters, blank_symbol):
    str_to_print = ""
    for x in random_word:
        if (x in used_letters):
            str_to_print+=x
            str_to_print+= " "
        else:
           str_to_print+=blank_symbol
           str_to_print+= " "
    print(f"Letters already used: {used_letters}")
    print(str_to_print)

# Construct a word dictionary
word_list = construct_dictionary()
SIZE=len(word_list)

#Randomly select word
new_word = select_new_word(word_list, SIZE).upper()

#Hangman
init_hangman()


#Input loop
input_letter = ''
while hangman_max_tries >= hangman_tries_left:
    print(f"Tries left {hangman_tries_left}")
    print_hangman(hangman_tries_left)
    print_word_with_blanks(new_word , used_letters, "_")
    print()
    print()

    #Just for testing
    print(new_word)

    #Prompt for letter and valdiate
    input_letter = input(prompt_message).upper()

    # Check for Quit
    if (input_letter==quit_message):
       break

    #Validate
    if input_letter.isalpha() == False:
        print("Input is invalid")
        continue
    if len(input_letter) != 1:
        print("Input only one letter")
        continue

    #Test letter, reduce tries
    used_letters.append(input_letter)
    if input_letter in new_word:
        print(f"Good guess!")
        correct_guesses.append(input_letter)
    else:
        print("Bad luck!")
        hangman_tries_left -=1
    
    #Check for game over
    print(f"Len new word {len(new_word)} len correct guesses {len(correct_guesses)}")
    if len(new_word) == len(correct_guesses):
        print("You win!  :-)")
        break

    if hangman_tries_left == 0:
       print("Game over!")
       break






 


