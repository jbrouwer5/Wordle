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
# nltk.download('words') -> Used to initially download the dictionary

import pygame

pygame.init()

size = width, height = 390, 510

# initalizes the screen
screen = pygame.display.set_mode(size)

# defines the colors for the self.board
black = 18, 18, 19
white = 255, 255, 255
dark_grey = 58, 58, 60
green = 83, 142, 78
yellow = 181, 159, 59

screen.fill(black)
pygame.display.flip()

# defines the tile and warning graphics for the self.board
font = pygame.font.SysFont(None, 50)
smallfont = pygame.font.SysFont(None, 20)


class Wordle:

    def __init__(self):
        self.current = True
        self.setofwords = set(words.words())  # nltk dictionary
        self.word = self.random_five_letter()
        self.letters = {}
        self.guesses = []
        self.feedback = ["", "", "", "", "", ""]
        self.winner = False

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

    def in_progress(self):
        return self.current

    def is_valid_guess(self, guess):
        is_english_word = guess.lower() in self.setofwords

        # if not is_english_word:
        #     print("Must be a valid english word\n")
        # if not is_five:
        #     print("Must be five letters long\n")

        return is_english_word

    def is_winner(self):
        return self.winner

    def make_guess(self, guess):

        result = self.make_feedback(guess)

        if result:
            print("You won!")
            self.current = False
            self.winner = True
            return 1

        if len(self.guesses) == 6:
            print("You weren't able to guess it.")
            self.current = False
            return -1

        return 0

    def make_feedback(self, newguess):
        guess = newguess.lower()
        curr_index = len(self.guesses)
        self.guesses.append(newguess)
        print(curr_index)
        letters_copy = {}

        for key in self.letters:
            letters_copy[key] = self.letters[key]

        for i in range(5):
            if guess[i] in letters_copy:
                if letters_copy[guess[i]] > 0:
                    letters_copy[guess[i]] -= 1
                    if guess[i] == self.word[i]:
                        self.feedback[curr_index] += "$"
                    else:
                        self.feedback[curr_index] += "*"
                else:
                    self.feedback[curr_index] += "."
            else:
                self.feedback[curr_index] += "."

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


def draw_wordle(wordle, current):

    # fills the screen with white
    screen.fill(black)
    for row in range(len(wordle.guesses)):
        for col in range(5):
            if wordle.feedback[row][col] == "$":
                color = green
            elif wordle.feedback[row][col] == "*":
                color = yellow
            else:
                color = dark_grey
            pygame.draw.rect(screen, color,
                             (50 + 60 * col, 50 + row * 60, 50, 50))
            letter = font.render(wordle.guesses[row][col], True, white)
            letterRect = letter.get_rect()
            letterRect.center = 50 + 60 * col + 25, 50 + row * 60 + 25
            screen.blit(letter, letterRect)

    if len(wordle.guesses) < 6:
        for i in range(len(current)):
            pygame.draw.rect(screen, dark_grey,
                             (50 + 60 * i, 50 + len(wordle.guesses) * 60, 50, 50))
            letter = font.render(current[i], True, white)
            letterRect = letter.get_rect()
            letterRect.center = 50 + 60 * i + \
                25, 50 + len(wordle.guesses) * 60 + 25
            screen.blit(letter, letterRect)

        for j in range(5 - len(current)):
            pygame.draw.rect(screen, dark_grey,
                             (50 + 60 * (j + len(current)), 50 + len(wordle.guesses) * 60, 50, 50))

    for row in range(len(wordle.guesses) + 1, 6):
        for col in range(5):
            pygame.draw.rect(screen, dark_grey,
                             (50 + 60 * col, 50 + row * 60, 50, 50))

    if not wordle.in_progress():
        if wordle.is_winner():
            end = invalidfont.render(
                "You won!", True, white)
        else:
            end = invalidfont.render(
                wordle.word, True, white)
        endRect = end.get_rect()
        endRect.center = 195, 10
        screen.blit(end, endRect)


# initalizes the game
game = Wordle()
curr_guess = ""
curr_length = 0
invalid_count = 0
draw_wordle(game, curr_guess)

# runs the game
while 1:

    pygame.key.start_text_input()

    # checks for quitting the tab and clicking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_BACKSPACE:
                if curr_length > 0:
                    curr_length -= 1
                    curr_guess = curr_guess[:-1]
            elif event.key == pygame.K_RETURN:
                if curr_length == 5:
                    if game.is_valid_guess(curr_guess):
                        game.make_guess(curr_guess)
                        curr_guess = ""
                        curr_length = 0
                    else:
                        invalid_count = 50
            else:
                if curr_length < 5:
                    curr_guess += chr(event.key).upper()
                    print(curr_guess)
                    curr_length += 1

    result = game.in_progress()
    draw_wordle(game, curr_guess)

    if invalid_count:
        print("invald")
        invalid = invalidfont.render(
            "Not in word list", True, white)
        invalidRect = invalid.get_rect()
        invalidRect.center = 195, 10
        screen.blit(invalid, invalidRect)
        invalid_count -= 1

    # checks if the game is over
    if not result:
        choice = None
        while (choice == None):
            draw_wordle(game, curr_guess)
            pygame.display.flip()
            print("Want to play again? Y/N")
            choice = input()
            if choice == "Y" or choice == "y":
                game = Wordle()
                result = True
                curr_guess = ""
                curr_length = 0
            elif choice == "N" or choice == "n":
                pygame.quit()

    # displays the self.board
    pygame.display.flip()
