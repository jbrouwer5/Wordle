# pip3 install pyyaml
# pip3 install random-word
from random import random
from random_word import RandomWords
from PyDictionary import PyDictionary

# to use system dictionary
import re

# to use nltk dictionary
from nltk.corpus import words
import nltk
# nltk.download('words')


class Wordle:

    def __init__(self):
        self.current = True
        self.setofwords = set(words.words())  # nltk dictionary
        self.word = self.random_five_letter()
        self.letters = {}
        self.guesses = []

        # file = open("/usr/share/dict/words", "r")
        # self.setofwords = re.sub("[^\w]", " ",  file.read()).split()
        # file.close()

        for i in range(len(self.word)):
            if self.word[i] in self.letters:
                self.letters[self.word[i]] += 1
            else:
                self.letters[self.word[i]] = 1

        # print(self.word)
        # print(self.letters)

        self.print_board()

    def in_progress(self):
        return self.current

    def is_valid_guess(self, guess):
        is_five = len(guess) == 5
        is_english_word = guess.lower() in self.setofwords

        if not is_english_word:
            print("Must be a valid english word\n")
        if not is_five:
            print("Must be five letters long\n")
        return is_english_word and is_five

    def make_guess(self):
        valid = False

        while not valid:
            print("Make a guess.\n")
            guess = input()
            valid = self.is_valid_guess(guess)

        result = self.make_feedback(guess)

        self.print_board()

        if result:
            print("You won!")
            self.current = False
            return

        if len(self.guesses) == 6:
            print("You weren't able to guess it.")
            self.current = False
            return

    def print_board(self):
        print()
        for word in self.guesses:
            print(word)

        for i in range(6-len(self.guesses)):
            print("------")

    def make_feedback(self, guess):
        curr_index = len(self.guesses)
        self.guesses.append(guess)
        self.guesses[curr_index] += " "

        letters_copy = {}

        for key in self.letters:
            letters_copy[key] = self.letters[key]

        for i in range(5):
            if guess[i] in letters_copy:
                if letters_copy[guess[i]] > 0:
                    letters_copy[guess[i]] -= 1
                    if guess[i] == self.word[i]:
                        self.guesses[curr_index] += "$"
                    else:
                        self.guesses[curr_index] += "*"
                else:
                    self.guesses[curr_index] += "."
            else:
                self.guesses[curr_index] += "."

        # print(self.word)
        # print(self.letters)

        if guess == self.word:
            return True
        return False

    def random_five_letter(self):
        dictionary = PyDictionary()
        r = RandomWords()

        word = None

        while word == None:
            word = r.get_random_word(minLength=5, maxLength=5)

        self.setofwords.add(word)
        return word


game = Wordle()

while game.in_progress():
    game.make_guess()
    print()
