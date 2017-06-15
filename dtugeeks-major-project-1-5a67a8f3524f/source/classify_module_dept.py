import os
import pickle
import time

import generate_training_and_test_data_dept as gttd
import nltk
import numpy as np
import ownModule
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB, BernoulliNB

training_data = gttd.get_training_data()
testing_data = gttd.get_test_data()
file_folder_outfile = ownModule.createFileFolder('outputFiles')
file_folder_outfile += os.path.sep


def get_classifier_NB(training_data):
    file_folder = ownModule.createFileFolder('classifiers')
    file_folder += os.path.sep
    fname = file_folder + "NB_classify"
    if os.path.isfile(fname):
        file_fp = open(file_folder + "NB_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        classifier = nltk.NaiveBayesClassifier.train(training_data)
        file_fp = open(file_folder + "NB_classify", "wb")
        pickle.dump(classifier, file_fp)
        file_fp.close()
        return classifier


def get_MNB(training_data):
    file_folder = ownModule.createFileFolder('classifiers')
    file_folder += os.path.sep
    fname = file_folder + "MNB_classify"
    # We need trainin data in the form of Numpy array
    # so the following processing needs to be done
    Y = [int(i[-1]) for i in training_data]
    training_data = [list(i) for i in training_data]
    lim = len(training_data)
    for i in range(0, lim):
        training_data[i] = list(training_data[i][0].values())
    X = training_data
    if os.path.isfile(fname):
        file_fp = open(file_folder + "MNB_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        cf = MultinomialNB()
        cf.fit(X, Y)
        file_fp = open(file_folder + "MNB_classify", "wb")
        pickle.dump(cf, file_fp)
        file_fp.close()
        return cf


def classify_with_MNB(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_MNB(training_data)

    t = cf.score(X, Y) * 100
    fp = open(file_folder_outfile + 'MNB_results.txt', 'w')
    results = cf.predict(X)
    for item in results:
        fp.write("%s\n" % item)
    return t


def get_BNB(training_data):
    file_folder = ownModule.createFileFolder('classifiers')
    file_folder += os.path.sep
    fname = file_folder + "BNB_classify"
    # We need trainin data in the form of Numpy array
    # so the following processing needs to be done
    Y = [int(i[-1]) for i in training_data]
    training_data = [list(i) for i in training_data]
    lim = len(training_data)
    for i in range(0, lim):
        training_data[i] = list(training_data[i][0].values())
    X = training_data
    if os.path.isfile(fname):
        file_fp = open(file_folder + "BNB_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        cf = BernoulliNB()
        cf.fit(X, Y)
        file_fp = open(file_folder + "BNB_classify", "wb")
        pickle.dump(cf, file_fp)
        file_fp.close()
        return cf


def classify_with_BNB(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_BNB(training_data)

    t = cf.score(X, Y) * 100
    fp = open(file_folder_outfile + 'BNB_results.txt', 'w')
    results = cf.predict(X)
    for item in results:
        fp.write("%s\n" % item)
    return t


def get_GNB(training_data):
    file_folder = ownModule.createFileFolder('classifiers')
    file_folder += os.path.sep
    fname = file_folder + "GNB_classify"
    # We need trainin data in the form of Numpy array
    # so the following processing needs to be done
    Y = [int(i[-1]) for i in training_data]
    training_data = [list(i) for i in training_data]
    lim = len(training_data)
    for i in range(0, lim):
        training_data[i] = list(training_data[i][0].values())
    X = training_data
    if os.path.isfile(fname):
        file_fp = open(file_folder + "GNB_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        cf = GaussianNB()
        cf.fit(X, Y)
        file_fp = open(file_folder + "GNB_classify", "wb")
        pickle.dump(cf, file_fp)
        file_fp.close()
        return cf


def classify_with_GNB(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_GNB(training_data)

    t = cf.score(X, Y) * 100
    fp = open(file_folder_outfile + 'GNB_results.txt', 'w')
    results = cf.predict(X)
    for item in results:
        fp.write("%s\n" % item)
    return t


def get_SVM(training_data):
    file_folder = ownModule.createFileFolder('classifiers')
    file_folder += os.path.sep
    fname = file_folder + "SVM_classify"
    # We need trainin data in the form of Numpy array
    # so the following processing needs to be done
    Y = [int(i[-1]) for i in training_data]
    training_data = [list(i) for i in training_data]
    lim = len(training_data)
    for i in range(0, lim):
        training_data[i] = list(training_data[i][0].values())
    X = training_data
    if os.path.isfile(fname):
        file_fp = open(file_folder + "SVM_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        cf = svm.SVC()
        cf.fit(X, Y)
        file_fp = open(file_folder + "SVM_classify", "wb")
        pickle.dump(cf, file_fp)
        file_fp.close()
        return cf


def classify_with_SVM(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_SVM(training_data)
    t = cf.score(X, Y) * 100
    fp = open(file_folder_outfile + 'SVM_results.txt', 'w')
    results = cf.predict(X)
    for item in results:
        fp.write("%s\n" % item)
    return t


def get_class_data():
    curr_location = os.getcwd()
    os.chdir('..')
    os.chdir('classifiers')
    try:
        command = 'rm BNB_classify MNB_classify GNB_classify NB_classify SVM_classify'
        os.system(command)
    finally:
        os.chdir(curr_location)
    all_algo = []
    start_time = time.time()
    svm_acc = classify_with_SVM(training_data, testing_data)
    svm_acc = ownModule.evaluate()
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("SVM", svm_acc, time_taken))
    print("SVM accuracy percent:", svm_acc)
    print("Time Taken by SVM in seconds : ", time_taken)
    start_time = time.time()
    nb_acc = nltk.classify.accuracy(get_classifier_NB(training_data), testing_data) * 100
    nb_acc = ownModule.evaluate()
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("NB", nb_acc, time_taken))
    print("NB Accuracy percent = ", nb_acc)
    print("Time Taken by NB in seconds : ", time_taken)
    start_time = time.time()
    # print("GaussianNB accuracy percent:",nltk.classify.accuracy(getget_classifier_GNB(training_data), testing_data)*100)
    gnb_acc = classify_with_GNB(training_data, testing_data)
    gnb_acc = ownModule.GNBEvaluate()
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("GNB", gnb_acc, time_taken))
    print("GNB accuracy percent:", gnb_acc)
    print("Time Taken by GaussianNB in seconds : ", time_taken)
    # print(all_algo)
    start_time = time.time()
    # print("GaussianNB accuracy percent:",nltk.classify.accuracy(getget_classifier_GNB(training_data), testing_data)*100)
    mnb_acc = classify_with_MNB(training_data, testing_data)
    mnb_acc = ownModule.evaluate()
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("MNB", mnb_acc, time_taken))
    print("MNB accuracy percent:", mnb_acc)
    print("Time Taken by MNB in seconds : ", time_taken)

    start_time = time.time()
    # print("GaussianNB accuracy percent:",nltk.classify.accuracy(getget_classifier_GNB(training_data), testing_data)*100)
    bnb_acc = classify_with_BNB(training_data, testing_data)
    bnb_acc = ownModule.evaluate()
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("MNB", bnb_acc, time_taken))
    print("BNB accuracy percent:", bnb_acc)
    print("Time Taken by BNB in seconds : ", time_taken)
    # print(all_algo)
    return all_algo


if __name__ == "__main__":
    get_class_data()
