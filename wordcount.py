# """Count words in file."""

from asyncore import read
import sys


# def tokenize(filename):
#     """Take file and create a list of words."""

#     opened_path = open(filename)

#     for line in opened_path:
#         line = line.rstrip()
#         words = line.split(" ")

#     return words


# def count_words(words):

#     word_counts = {}

#     for word in words:
#         word = word.lower().strip(",")
#         word_counts[word] = word_counts.get(word, 0) + 1

#     return word_counts


# def print_word_counts(word_counts):

#     for word, count in word_counts.items():
#         print(word, count)


# filename1 = sys.argv[1]
# filename2 = sys.argv[2]

""" Opens a file and counts the times a word occurs"""


def word_count(file=sys.argv[1]):

    file = open(file)

    word_count = {}

    for line in file:
        line = line.rstrip(",")
        words = line.split()

        for word in words:
            word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    for key, value in word_count.items():
        print(key, value)

    file.close()


word_count()
