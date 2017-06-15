import generate_training_and_test_data_dept as gttd
import nltk
import ownModule
from nltk.classify import ClassifierI
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        empty_dict = {}
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
            try:
                empty_dict[v] += 1
            except:
                empty_dict[v] = 1
        lit = sorted(empty_dict)
        return lit[0]

def main():

    training_set = gttd.get_training_data()
    testing_set = gttd.get_test_data()
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    # print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
    NB_accuracy = ownModule.evaluate()
    print("Original Naive Bayes Algo accuracy percent:", NB_accuracy)
    MNB_classifier = SklearnClassifier(MultinomialNB())
    MNB_classifier.train(training_set)
    # print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)
    MNB_accuracy = ownModule.evaluate()
    print("MNB_classifier accuracy percent:", MNB_accuracy)
    BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
    BernoulliNB_classifier.train(training_set)
    # print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)
    BNB_accuracy = ownModule.evaluate()
    print("BernoulliNB_classifier accuracy percent:", BNB_accuracy)
    voted_classifier = VoteClassifier(classifier,
                                      MNB_classifier,
                                      BernoulliNB_classifier)
    # print("Voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)
    combined_accuracy = ownModule.Vevaluate()
    print("Voted_classifier accuracy percent:", combined_accuracy)
    accuracy_list = list()
    accuracy_list.append(NB_accuracy)
    accuracy_list.append(MNB_accuracy)
    accuracy_list.append(BNB_accuracy)
    accuracy_list.append(combined_accuracy)
    return accuracy_list

if __name__ =='__main__':
    main()
