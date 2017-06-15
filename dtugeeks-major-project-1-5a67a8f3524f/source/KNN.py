__author__ = 'vikas'
import csv
import math
import os

import nltk
import ownModule
from nltk.corpus import stopwords as stw
from nltk.stem.porter import *
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.semi_supervised import LabelPropagation


def main():
    stemmer = PorterStemmer()
    file_folder = ownModule.createFileFolder('outputFiles')
    file_folder += os.path.sep
    fp = open(file_folder + "First1000.csv", "r", encoding="utf-8")
    input_reader = csv.reader(fp, delimiter="|")
    input_reader = [row[0] for row in input_reader]

    feature_set = []
    all_words = {}

    stopwords = stw.words('english')
    # Count the occurence of each word in all of the labelled documents
    for i in input_reader:
        m = sent_tokenize(i)
        for k in m:
            words = nltk.tokenize.word_tokenize(k)
            for word in words:
                if word not in stopwords:
                    try:
                        all_words[stemmer.stem(word.lower())] += 1
                    except:
                        all_words[stemmer.stem(word.lower())] = 1

    file_handle = open(file_folder + "Unlabelled Posts.txt", "r", encoding="utf-8")
    file_handle = file_handle.readlines()[0:1000]
    # Count the occurence of each word in all of the unlabelled documents

    for i in file_handle:
        temp = i[1:]
        temp = temp[:-1]
        m = sent_tokenize(temp)
        for k in m:
            words = nltk.tokenize.word_tokenize(k)
            for word in words:
                if word not in stopwords:
                    try:
                        all_words[stemmer.stem(word.lower())] += 1
                    except:
                        all_words[stemmer.stem(word.lower())] = 1
    # total number of documents
    total_docs = len(input_reader) + len(file_handle)
    # total number of words
    total_words = len(all_words)
    feature_set = []
    for i in input_reader:
        m = sent_tokenize(i)
        for k in m:
            words = nltk.tokenize.word_tokenize(k)
            word_list = {}
            for word in words:
                if word not in stopwords:
                    try:
                        word_list[stemmer.stem(word.lower())] += 1
                    except:
                        word_list[stemmer.stem(word.lower())] = 1
        # Now for every word in all of the documents
        temp_features = []
        for key, val in all_words.items():
            try:
                temp_features.append(word_list[key] * math.log(total_docs / all_words[key]))
            except:
                temp_features.append(0)
        feature_set.append(temp_features)

    # Now do it for unlabelled data

    for i in file_handle:
        temp = i[1:]
        temp = temp[:-1]
        m = sent_tokenize(temp)
        for k in m:
            words = nltk.tokenize.word_tokenize(k)
            word_list = {}
            for word in words:
                if word not in stopwords:
                    try:
                        word_list[stemmer.stem(word.lower())] += 1
                    except:
                        word_list[stemmer.stem(word.lower())] = 1
        # Now for every word in all of the documents
        temp_features = []
        for key, val in all_words.items():
            try:
                temp_features.append(word_list[key] * math.log(total_docs / all_words[key]))
            except:
                temp_features.append(0)
        feature_set.append(temp_features)

    file_handle = [i[1:-1] for i in file_handle]
    newlist = input_reader + file_handle
    feature_extraction = CountVectorizer(stop_words='english')
    x = feature_extraction.fit_transform(newlist).toarray()
    label_prop_model = LabelPropagation(kernel='knn')
    # read the labels
    ans_reader = open(file_folder + "labels_of_data_department.csv", "r")
    ans_csv = csv.reader(ans_reader, delimiter="|")
    ans_reader = [int(row[0]) for row in ans_csv]
    for i in file_handle:
        ans_reader.append(-1)
    print(len(ans_reader))
    t = label_prop_model.fit(x, ans_reader)

    accuracy = ownModule.Vevaluate()
    print("Accuracy of Semi Supervised Learning:", accuracy)
    return accuracy

if __name__ =='__main__':
    main()
