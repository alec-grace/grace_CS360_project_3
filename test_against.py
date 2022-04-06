# File: test_against.py
# Author: Alec Grace
# Created on: 6 April 2022
# Purpose:
#   class to be used in main.py for CS360 Project 3
from file_reader import FileReader
import math


class TestAgainst:

    # Takes training file and test file as input, calls private methods to
    # extract the required data and returns the result
    def __init__(self, training_file: str, test_file: str):
        self.training_file = training_file
        self.test_file = test_file
        self.author_training = FileReader(training_file)
        self.testing = FileReader(test_file)
        self.data = self.__run_test()

    # Does the actual testing of the training file against the test file
    def __run_test(self):
        # set up necessary info before testing files
        frequencies = []
        default_probability = 2 ** -15
        # check each gram in the testing file for its frequency in the training data
        for gram in self.testing.author_grams:
            if gram[0] == '<sol>':
                frequencies.append(self.author_training.word_freq('<sol>'))
            elif gram[0] in self.author_training.word_tracker.keys():
                for val_list in self.author_training.word_tracker[gram[0]]:
                    if val_list[0] == gram[1]:
                        freq = self.author_training.local_freq(gram[0], gram[1])
                        frequencies.append(freq)
            else:
                frequencies.append(default_probability)
        # add up all the logs of frequencies to get total probability
        running_total = 0
        for frequency in frequencies:
            running_total += math.log(frequency)
        # return author name and frequency results
        return [self.__get_author_name(), running_total]

    # Parses the training file name to get authors name
    def __get_author_name(self):
        return self.training_file.split('-')[0]
