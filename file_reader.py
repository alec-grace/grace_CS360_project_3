# File: main.py
# Author: Alec Grace
# Created on: 1 April 2022
# Purpose:
#   class to be used in main.py for CS360 Project 3
import math


class FileReader:

    # Constructor parses file into grams and then, if it is a training
    # file, generates a word-tracker dictionary that keeps track of
    # which words come after each unique word and how many times that
    # happens in the whole file
    def __init__(self, filename: str, filetype='train'):
        self.word_frequencies = {}
        self.total_words = 0
        self.author_grams = []
        self.filetype = filetype
        with open(filename, 'r') as author_file:
            lines = author_file.readlines()
            for line in lines:
                line = line.rstrip('\n')
                line = '<sol>,' + line + ',<eol>'
                split_line = line.split(',')
                for i in range(len(split_line) - 1):
                    self.author_grams.append((split_line[i], split_line[i + 1]))
                self.total_words += len(split_line)
        author_file.close()

        if self.filetype == 'train':
            self.word_tracker = {}
            for gram in self.author_grams:
                locator = False
                if gram[0] not in self.word_tracker.keys():
                    self.word_tracker[gram[0]] = [[gram[1], 1]]
                    self.word_frequencies[gram[0]] = 1
                else:
                    self.word_frequencies[gram[0]] += 1
                    for duo_list in self.word_tracker[gram[0]]:
                        if duo_list[0] == gram[1]:
                            duo_list[1] += 1
                            locator = True
                    if not locator:
                        self.word_tracker[gram[0]].append([gram[1], 1])

    # Debugging method to show result of specific word in word_tracker
    def word_result(self, target: str):
        if self.filetype == 'train':
            for pair in self.word_tracker[target]:
                print(pair)

    # Returns total frequency of a word in the file
    def word_freq(self, word: str):
        return self.word_frequencies[word] / self.total_words

    # Returns frequency of w2 in the list of all words coming after w1
    def local_freq(self, w1: str, w2: str):
        total = 0
        frequency = 0
        default_probability = math.log(2 ** -15)
        locator = False
        for val_list in self.word_tracker[w1]:
            total += val_list[1]
            if val_list[0] == w2:
                locator = True
                frequency = val_list[1]
        if not locator:
            if w2 in self.word_tracker.keys():
                return self.word_freq(w2)
            else:
                return default_probability
        else:
            return frequency / total
