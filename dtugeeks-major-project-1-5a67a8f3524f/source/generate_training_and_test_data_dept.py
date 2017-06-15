__author__ = 'vikas'
import csv
import os

import extract_features as ef
import nltk
import ownModule
from nltk.tokenize import sent_tokenize

file_folder = ownModule.createFileFolder('outputFiles')
file_folder += os.path.sep
fp = open(file_folder + "First1000.csv", "r", encoding="utf-8")
input_reader = csv.reader(fp, delimiter="|")
#input_data = input_reader
input_reader = [row[0] for row in input_reader]
input_reader = input_reader
feature_set = []
for i in input_reader:
    m = sent_tokenize(i)
    word_list = []
    for k in m:
        words = nltk.tokenize.word_tokenize(k)
        for word in words:
            word_list.append(word.lower())
    feature_set.append(word_list)

ans_reader = open(file_folder + "labels_of_data_department.csv", "r")
ans_csv = csv.reader(ans_reader, delimiter="|")
ans_reader = [row for row in ans_csv]

for i in range(0, len(ans_reader)):
    feature_set[i].append(ans_reader[i][0])
feature_sets = ef.get_feature_list(feature_set)


def get_training_data():
    return feature_sets[:700]


def get_test_data():
    return feature_sets[700:]


def get_input_data():
    return input_reader
