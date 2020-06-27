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
        self.incorrect_letters = []
        self.lives = 6
        self.dev_mode = mode
        self.status = ""
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
            self.status = "win"
        elif len(guess) == 1 and guess in self.secret:
            self.known_letters.append(guess)
            # if all letters guessed
            if sorted(list(set(self.secret))) == sorted(list(set(self.known_letters))):
                self.status = "win"
        else:
            self.lives -= 1
            if len(guess) == 1:
                self.incorrect_letters.append(guess)
            if self.lives == 0:
                self.status = "lose"


    def print_screen_head(self):
        os.system('cls' if os.name=='nt' else 'clear')
        for line in self.title:
            print(line)

        response = []

        print("\n\n")

        if len(self.incorrect_letters) != 0:
            print("Wrong guesses so far: " + "-".join(sorted(list(set(self.incorrect_letters)))))
            print("\n\n")

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


def main_game(game):
    # main game loop
    while game.status == "":
        game.print_screen_head()
        game.check_guess(input("\nEnter a letter or guess the whole word: ").lower())

    # End of Game
    game.print_screen_head()
    if game.status == "win":
        print("\nYOU WIN!")
        print("\nThe word was "+ "".join(game.secret).upper())
    elif game.status == "lose":
        print("\nYOU LOSE!")
        print("\nThe word was "+ "".join(game.secret).upper())


def game_setup(dev_mode = False):

    os.system('cls' if os.name=='nt' else 'clear')

    # Choose player number
    while True:
        players = int(input("How many players? (\"1\" or \"2\"): "))
        if players == 1:
            # choose difficulty
            while True:
                game_mode = input("\nEasy (e), or hard (h)? ").lower()
                if game_mode == 'e':
                    game = HangMan(easy_mode(), dev_mode)
                    break
                elif game_mode == 'h':
                    game = HangMan(hard_mode(), dev_mode)
                    break
                else:
                    print("Not a valid response, please try again")
            break
        elif players == 2:
            secret = input("Enter the secret word: ").lower()
            game = HangMan(secret, dev_mode)
            break
        else:
                print("Not a valid response, please try again")

    main_game(game)


try:
    dev_mode = False
    if len(sys.argv) == 2 and sys.argv[1] == 'd':
        dev_mode = True
    game_setup(dev_mode)    
    input("Press Enter to exit ...")
except KeyboardInterrupt:
    print("\n\nexiting ...")
    SystemExit