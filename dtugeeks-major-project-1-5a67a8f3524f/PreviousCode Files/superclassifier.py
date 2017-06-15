__author__ = 'prakhardogra'

import ownModule
import nltk
import generate_training_and_test_data_dept as gttd
import csv
import os
import pickle
import time
import itertools
import operator

from superclassify import NB
from superclassify import MNB
from superclassify import BNB
#from superclassify import SVM

start_time = time.time()

training_data = gttd.get_training_data()
testing_data = gttd.get_test_data()
input_data = gttd.get_input_data()

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]


file_folder = ownModule.createFileFolder('outputFiles')
file_folder += os.path.sep


ans_reader = open(file_folder + "labels_of_data_department.csv", "r")
ans_csv = csv.reader(ans_reader, delimiter="|")
ANS = []

MNB = MNB(training_data, testing_data)
NB = NB(training_data, testing_data)
BNB = BNB(training_data, testing_data)
#SVM = SVM(training_data, input_data)

'''

mnb = open(file_folder + 'MNB_results.txt', 'r')
bnb = open(file_folder + 'BNB_results.txt', 'r')
nb = open(file_folder + 'NB_results.txt', 'r')
svm = open(file_folder + 'SVM_results.txt', 'r')



for type in mnb:
    MNB.append(type.split("\n")[0])
#print(len(MNB))
for type in nb:
    NB.append(type.split("\n")[0])
#print(len(NB))
for type in bnb:
    BNB.append(type.split("\n")[0])
#print(len(BNB))
for type in svm:
    SVM.append(type.split("\n")[0])
#print(len(SVM))
'''
i = 0
for type in ans_csv:
    i += 1
    if i > 700:
        ANS.append(type[0])


MYANS = []
myans = open(file_folder + "MYANS_results.txt","w")         #stores d results for future...not that it matters ...LOL

for i in range(300):
    MYANS.append(most_common([MNB[i],BNB[i],NB[i]])) #priority by accuracy from previous iterations
for i in range(300):
    myans.write(MYANS[i])
count = 0
for i in range(300):
    if ANS[i] == MYANS[i]:
        count += 1

accuracy = float(count)/3.0

end_time = time.time()
time_taken = end_time - start_time

print(accuracy,time_taken)
