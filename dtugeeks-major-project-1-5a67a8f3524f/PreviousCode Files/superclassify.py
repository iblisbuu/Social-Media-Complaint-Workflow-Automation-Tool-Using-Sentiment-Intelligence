__author__ = 'prakhardogra'
import os
import pickle
import time

import generate_training_and_test_data_dept as gttd
import nltk
import numpy as np
import ownModule
from nltk.tokenize import sent_tokenize

'''
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn import svm
#from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
'''
from classify_module_dept import get_classifier_NB
from classify_module_dept import get_MNB
from classify_module_dept import get_BNB
from classify_module_dept import get_SVM

training_data = gttd.get_training_data()
testing_data = gttd.get_test_data()
input_data = gttd.get_input_data()

file_folder = ownModule.createFileFolder('outputFiles')
file_folder += os.path.sep

def MNB(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_MNB(training_data)

    #t = cf.score(X, Y) * 100
    #fp = open(file_folder_outfile + 'MNB_results.txt', 'w')
    results = []
    for i in training_data:
        results.append(cf.classify(i[0]))
    #for item in results:
    #    fp.write("%s\n" % item)
    return results

def BNB(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_BNB(training_data)

    #t = cf.score(X, Y) * 100
    #fp = open(file_folder_outfile + 'BNB_results.txt', 'w')
    results = []
    for i in training_data:
        results.append(cf.classify(i[0]))
    #for item in results:
    #    fp.write("%s\n" % item)
    return results

def NB(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_classifier_NB(training_data)

    #t = cf.score(X, Y) * 100
    #fp = open(file_folder_outfile + 'GNB_results.txt', 'w')
    results = []
    for i in training_data:
        results.append(cf.classify(i[0]))
    #for item in results:
    #    fp.write("%s\n" % item)
    return results

'''
def SVM(training_data, input_data):

    cf = get_SVM(training_data)
    #t = cf.score(X, Y) * 100
    #fp = open(file_folder_outfile + 'SVM_results.txt', 'w')

    results = []
    for i in input_data:
        #print(i)
        m = sent_tokenize(i)

        word_list = []
        feature_set = []
        for k in m:
            words = nltk.tokenize.word_tokenize(k)
            for word in words:
                word_list.append(word.lower())
        feature_set.append(word_list)
        results.append(cf.predict(feature_set))

    #results.append(cf.predict())

    #for item in results:
    #    fp.write("%s\n" % item)
'''