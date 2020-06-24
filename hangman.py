import os
import random
import sys


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


class HangMan:
    def __init__(self, secret, mode = False):
        self.secret = list(secret)
        self.known_letters = []
        self.lives = 6
        self.dev_mode = mode
        self.win = False
        self.title = []
        self.hangman = []

        with open("Art/titleAscii", "r") as title_file:
            for line in title_file:
                self.title.append(line.rstrip())

        with open("Art/HangmanAscii", "r") as hangman_file:
            for line in hangman_file:
                self.hangman.append(line.rstrip())
    

    def check_guess(self, guess):
        if list(guess) == self.secret:
            self.win = True
        elif len(guess) == 1 and guess in self.secret:
            self.known_letters.append(guess)
        else:
            self.lives -= 1
            if self.lives == 0:
                print("\nYOU LOSE!")
                print("\nThe word was "+ "".join(self.secret).upper())
                return False


    def print_screen_head(self):
        os.system('cls' if os.name=='nt' else 'clear')
        for line in self.title:
            print(line)
        
        print("\n\n")

        response = []

        for letter in self.secret:
            if letter in self.known_letters:
                response.append(letter)
            else:
                response.append(" _ ")
        if self.dev_mode == True:
            print("The word is: " + "".join(self.secret) + "\n\n")

        print("".join(response).upper())

        print("\n\n")

        for i in range((((self.lives + 1)* 7)-7), ((self.lives + 1)* 7), 1):
            print (self.hangman[i])
        pass


def game(dev_mode = False):
    game_mode = input("\nEasy (e), or hard (h)? ").lower()
    if game_mode == 'e':
        game = HangMan(easy_mode(), dev_mode)
    elif game_mode == 'h':
        game = HangMan(hard_mode(), dev_mode)
    
    game.print_screen_head()
    game.check_guess(input("\nEnter a letter or guess the whole word: ").lower())
    game.print_screen_head()
    


try:
    dev_mode = False
    if len(sys.argv) == 2 and sys.argv[1] == 'd':
        dev_mode = True
    game(dev_mode)    
    input("Press Enter to exit ...")
except KeyboardInterrupt:
    print("\n\nexiting ...")
    SystemExit
