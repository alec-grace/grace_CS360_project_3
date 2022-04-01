# File: main.py
# Author: Alec Grace
# Created on: 26 Feb 2022
# Purpose:
#   driver for CS360 Project 3: Author Prediction Using Bayesian Analysis

def main():

    sentences = []
    babbage_grams = []
    with open('babbage-train.txt', 'r') as babbage_file:
        lines = babbage_file.readlines()
        for line in lines:
            line = line.rstrip('\n')
            line = '<sol>,' + line + ',<end>'
            split_line = line.split(',')
            sentences.append(split_line)
    babbage_file.close()

    for line in sentences:
        for i in range(len(line) - 1):
            babbage_grams.append((line[i], line[i + 1]))

    word_counter = {}
    for gram in babbage_grams:
        if gram[0] not in word_counter.keys():
            word_counter[gram[0]] = [[gram[1], 1]]
        else:
            for duo_list in word_counter[gram[0]]:
                if duo_list[0] == gram[1]:
                    duo_list[1] += 1
    # figure out how to add a new list to the value list

    print(word_counter['THE'])


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

