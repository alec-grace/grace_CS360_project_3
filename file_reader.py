# File: main.py
# Author: Alec Grace
# Created on: 1 April 2022
# Purpose:
#   class to be used in main.py for CS360 Project 3

class FileReader:
    
    def __init__(self, filename: str):
        self.word_frequencies = {}
        self.total_words = 0
        self.author_grams = []
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

    def word_result(self, target: str):
        for pair in self.word_tracker[target]:
            print(pair)

    def word_freq(self, word: str):
        return self.word_frequencies[word] / self.total_words

    def local_freq(self, w1: str, w2: str):
        total = 0
        frequency = 0
        for val_list in self.word_tracker[w1]:
            total += val_list[1]
            if val_list[0] == w2:
                frequency = val_list[1]
        return frequency / total
