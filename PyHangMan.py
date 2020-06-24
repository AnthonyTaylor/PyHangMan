import random
import sys

def clear_screen():
    import os
    os.system('cls' if os.name=='nt' else 'clear')


def hard_mode():
    import json
    with open("Data/hard.json", "r") as word_file:
        word_list = json.load(word_file)
    secret = random.choice(list(word_list))
    return list(secret)


def easy_mode():
    with open("Data/easy.txt", "r") as word_file:
        word_list = word_file.readlines()
    secret = random.choice(word_list).rstrip()
    return list(secret)


def print_hangman(lives):
    with open("Art/HangmanAscii", "r") as hangman_file:
        hangman_lines = hangman_file.readlines()
        for i in range((((lives + 1)* 7)-7), ((lives + 1)* 7), 1):
            print (hangman_lines[i].rstrip())


def print_word(guess, secret, known_letters):
    if guess is not "":
        print(guess.upper() + " in in the word")

    response = []

    for letter in secret:
        if letter in known_letters:
            response.append(letter)
        else:
            response.append("_ ")
    
    print("".join(response).upper())

    if response == secret:
        print("\nYOU WIN")
        return "win" 
    else:
         return "no win"
   

def print_title():
    with open("Art/titleAscii", "r") as title_file:
        for line in title_file:
            print(line.rstrip())


def game(dev_mode = False):
    secret = []
    known_letters = []
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
        guess = ""
        print("you have " + str(lives) + " lives remaining")
        print_hangman(lives)
        print_word(guess, secret, known_letters)
        guess = input("\nEnter a letter or guess the whole word: ").lower()

        if list(guess) == secret:
            keep_going = False
            print("\nYOU WIN")
        elif len(guess) == 1 and guess in secret:
            known_letters.append(guess)
            if print_word(guess, secret, known_letters) == "win":
                break
        else:
            lives -= 1
            if lives == 0:
                print_hangman(lives)
                print("\nYOU LOSE!")
                print("\nThe word was "+ "".join(secret).upper())
                keep_going = False
            

try:
    dev_mode = False
    if len(sys.argv) == 2 and sys.argv[1] == 'd':
        dev_mode = True
    game(dev_mode)    
    input("Press Enter to exit ...")
except KeyboardInterrupt:
    print("\n\nexiting ...")
    SystemExit
