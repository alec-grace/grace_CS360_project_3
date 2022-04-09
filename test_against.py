# File: test_against.py
# Author: Alec Grace
# Created on: 6 April 2022
# Purpose:
#   class to be used in main.py for CS360 Project 3
from file_reader import FileReader
import math


class TestAgainst:

    # Cache each new file read so there is no repeat calculations/reading
    training_file_cache = {}
    test_file_cache = {}

    # Takes training file and test file as input, calls private methods to
    # extract the required data and returns the result
    def __init__(self, training_file: str, test_file: str):
        self.training_file = training_file
        self.test_file = test_file
        if self.__get_train_author_name() in TestAgainst.training_file_cache.keys():
            self.author_training = TestAgainst.training_file_cache[self.__get_train_author_name()]
        else:
            self.author_training = FileReader(training_file)
            TestAgainst.training_file_cache[self.__get_train_author_name()] = self.author_training
        if self.training_file in TestAgainst.test_file_cache.keys():
            self.test_file = TestAgainst.test_file_cache[self.training_file]
        else:
            self.testing = FileReader(test_file, 'test')
            TestAgainst.test_file_cache[self.test_file] = self.testing
            
        self.data = self.__run_test()

    # Does the actual testing of the training file against the test file
    def __run_test(self):
        # set up necessary info before testing files
        frequencies = []
        default_probability = math.log(2 ** -15)
        # check each gram in the testing file for its frequency in the training data
        for gram in self.testing.author_grams:
            if gram[0] == '<sol>':
                frequencies.append(self.author_training.word_freq('<sol>'))
            if gram[0] in self.author_training.word_tracker.keys():
                for val_list in self.author_training.word_tracker[gram[0]]:
                    if val_list[0] == gram[1]:
                        freq = self.author_training.local_freq(gram[0], gram[1])
                        frequencies.append(math.log(freq))
            else:
                frequencies.append(default_probability)
        # add up all the logs of frequencies to get total probability
        running_total = sum(frequencies)
        # return author name and frequency results
        return [self.__get_train_author_name(), running_total]

    # Parses the training file name to get authors name
    def __get_train_author_name(self):
        return self.training_file.split('-')[0].capitalize()
