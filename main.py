# File: main.py
# Author: Alec Grace
# Created on: 26 March 2022
# Purpose:
#   driver for CS360 Project 3: Author Prediction Using Bayesian Analysis
from test_against import TestAgainst


def main():
    # create variables for file names (easier to use)
    b_train = 'babbage-train.txt'
    b_test = 'babbage-test.txt'
    p_train = 'poe-train.txt'
    p_test = 'poe-test.txt'
    f_train = 'freud-train.txt'
    f_test = 'freud-test.txt'
    # put the training and test files into lists so it's easier
    training = [b_train, p_train, f_train]
    testing = [b_test, p_test, f_test]

    # create training data for each author for each test
    for test_file in testing:
        current_low = None
        low_author = ''
        for author in training:
            current = TestAgainst(author, test_file)
            print("Author: " + str(current.data[0].capitalize()) + " tested against "
                  + test_file + " results in " + str(current.data[1]))
            if current_low is None or current_low < current.data[1]:
                current_low = current.data[1]
                low_author = str(current.data[0].capitalize())
        print('\n' + low_author + " is most likely the author of " + test_file + '\n')


if __name__ == "__main__":
    main()
