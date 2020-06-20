import random
import sys

def clear_screen():
    import os
    os.system('cls' if os.name=='nt' else 'clear')


def hard_mode():
    import json
    with open("Data/words_dictionary.json", "r") as word_file:
        word_list = json.load(word_file)
    secret = random.choice(list(word_list))
    return list(secret)


def easy_mode():
    with open("Data/simpleWords.txt", "r") as word_file:
        word_list = word_file.readlines()
    secret = random.choice(word_list).rstrip()
    return list(secret)


def print_hangman(lives):
    with open("Art/HangmanAscii", "r") as hangman_file:
        hangman_lines = hangman_file.readlines()
        for i in range((((lives + 1)* 7)-7), ((lives + 1)* 7), 1):
            print (hangman_lines[i])


def print_word(guess, secret):
    print(guess.upper() + " in in the word")
    

def print_title():
    with open("Art/titleAscii", "r") as title_file:
        for line in title_file:
            print(line)


def game(dev_mode = False):
    secret = []
    print_title()
    game_mode = input("\nEasy (e), or hard (h)? ").lower()
    if game_mode == 'e':
        secret = easy_mode()
    elif game_mode == 'h':
        secret = hard_mode()

    word_length = len(secret)
    print("\nThere are " + str(word_length) + " letters")
    if dev_mode:
        print ("".join(secret))

    keep_going = True
    lives = 6

    while keep_going:
        # clear_screen()
        print("you have " + str(lives) + " lives remaining")
        print_hangman(lives)
        guess = input("\nEnter a letter or guess the whole word: ").lower()

        if list(guess) == secret:
            keep_going = False
            print("\nYOU WIN")
        elif len(guess) == 1 and guess in secret:
            print_word(guess, secret)
        else:
            lives -= 1

            if lives == 0:
                print_hangman(lives)
                print("\nYOU LOSE!")
                print("\nThe word was "+ "".join(secret).upper())
                keep_going = False


try:
    if len(sys.argv) == 2 and sys.argv[1] == 'd':
        dev_mode = True
    game(dev_mode)    
except KeyboardInterrupt:
    print("\n\nexiting ...")
    SystemExit
