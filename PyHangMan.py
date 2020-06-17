import json
import random

def hard_mode():
    with open("Data/words_dictionary.json", "r") as word_file:
        word_list = json.load(word_file)
    secret = random.choice(list(word_list))
    return list(secret)


def easy_mode():
    with open("Data/simpleWords.txt", "r") as word_file:
        word_list = word_file.readlines()
    secret = random.choice(word_list).rstrip()
    return list(secret)


def print_output(guess, secret):
    print(guess + " in in the word")


secret = []
game_mode = input("Easy (e), or hard (h)? ")
if game_mode == 'e':
    secret = easy_mode()
elif game_mode == 'h':
    secret = hard_mode()

word_length = len(secret)
print("There are " + str(word_length) + " letters")
print (secret)

keep_going = True
lives = 1

while keep_going:
    guess = input("enter a letter or guess the whole word: ")
    if list(guess) == secret:
        keep_going = False
        print("YOU WIN")
    elif len(guess) == 1 and guess in secret:
        print_output(guess, secret)
    else:
        lives -= 1
        if lives == 0:
            print("you lose!")
            print("The word was "+ "".join(secret).upper())
            keep_going = False
        else:
            print("incorrect, lose a life")
