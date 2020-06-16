import json
import random

'''
    with open("Data/words_dictionary.json", "r") as word_file:
        word_list = json.load(word_file)
    secret = random.choice(list(word_list))
    print (secret)
'''

with open("Data/simpleWords.txt", "r") as word_file:
    word_list = word_file.readlines()
secret = random.choice(word_list).rstrip()
word_length = len(secret)
print("There are " + str(word_length) + " letters")
print (secret)
