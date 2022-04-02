# File: main.py
# Author: Alec Grace
# Created on: 26 March 2022
# Purpose:
#   driver for CS360 Project 3: Author Prediction Using Bayesian Analysis
from file_reader import FileReader


def main():

    babbage_info = FileReader('babbage-train.txt')
    freud_info = FileReader('freud-train.txt')
    poe_info = FileReader('poe-train.txt')

    freud_info.word_result('IN')
    print(babbage_info.total_words)
    print(freud_info.total_words)
    print(poe_info.total_words)


if __name__ == "__main__":
    main()


# dictionary of all seen words in one corpus:
# Key: unique word
# Value: list of lists [2] [next word, # of occurrences]
#
# EX: dict = {
#       'THE' : ['CAT', 2], ['RAT', 4], ['MAT', 1]
#
# a^x = y, log(base a) y = x
# P(a) = 0.125 (1/8)
# log (base 2) P(a) = -3

# x * y = z
# log(xy) = log(z)
# log(x) + log(y) = log(xy) = log(z)
#

# p(a) * p(b) * p(c) ... = log(a) + log(b) + log(c) ...
# x > y
# log(x) > log(y)

