# Wordle
By Jackson Brouwer 

This repository contains two implementations of the popular game Wordle. 

The first version is a CLI wordle game, where input and output is given in ASCII characters on the command line. 
The second version is a graphical interface game, where it takes keyboard input and replicates the functions of the wordle game. 

To use the nltk dictionary set that I used, include the following lines in your file. 
Warning, this dictionary does not support plural words. 

from nltk.corpus import words
import nltk
nltk.download('words')


# Graphical Wordle 
This program uses the pygame library for graphics. Install and import pygame to support this program. 

How to play:
Type input into keyboard. If you have a five letter word written, press enter and the game will give you the appropriate color feedback. 
Green - Correct letter and place
Yellow - Correct letter wrong place
Grey - Incorrect letter 

If you guess the word the game will let you know that you have won. 
If you run out of guesses it will tell you what the secret word was.

<img width="381" alt="Screen Shot 2022-05-08 at 2 01 37 PM" src="https://user-images.githubusercontent.com/63489213/167312195-1829dd4a-b026-4784-86b7-eab3655c2c97.png">

<img width="383" alt="Screen Shot 2022-05-08 at 2 04 12 PM" src="https://user-images.githubusercontent.com/63489213/167312200-99a32764-61a6-4ca7-b732-9ba05a315e26.png">

<img width="388" alt="Screen Shot 2022-05-08 at 2 02 48 PM" src="https://user-images.githubusercontent.com/63489213/167312198-33959f4c-fdbc-4cfe-9440-fbd7f3a928b7.png">

