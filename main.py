# File: main.py
# Author: Alec Grace
# Created on: 26 March 2022
# Purpose:
#   driver for CS360 Project 3: Author Prediction Using Bayesian Analysis
from file_reader import FileReader
import math


def main():
    # create training data for each author
    babbage_train = FileReader('babbage-train.txt')
    freud_train = FileReader('freud-train.txt')
    poe_train = FileReader('poe-train.txt')
    test_train = FileReader('test-train.txt')

    # separate the test file into grams
    babbage_test = FileReader('babbage-test.txt')

    # testing stuff
    test_grams = [['HELLO', 'GLOBE'], ['ANTONIO', 'PIZZA'], ['ONE', 'HUNDRED'],
                  ['IN', 'A'], ['WHICH', 'ARE'], ['DERIVED', 'LITTLE']]

    # set up necessary info before testing files
    frequencies = []
    default_probability = 2 ** -15
    for gram in babbage_test.author_grams:
    # for gram in test_grams:
        if gram[0] == '<sol>':
            frequencies.append(babbage_train.word_freq('<sol>'))
        elif gram[0] in babbage_train.word_tracker.keys():
            for val_list in babbage_train.word_tracker[gram[0]]:
                if val_list[0] == gram[1]:
                    freq = babbage_train.local_freq(gram[0], gram[1])
                    frequencies.append(freq)
        else:
            frequencies.append(default_probability)

    running_total = 0
    for thing in frequencies:
        running_total += math.log(thing)

    print(running_total)


if __name__ == "__main__":
    main()

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
