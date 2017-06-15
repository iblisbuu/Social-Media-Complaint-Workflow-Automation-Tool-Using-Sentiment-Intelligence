__author__ = 'vikas'
import random
import shelve
import nltk


# this function takes a list of string and returns a set of features
def get_feature_list(documents):
    word_lists = shelve.open("word_list")
    random.shuffle(documents)
    try:
        all_words = word_lists['words']
    except:
        all_words = []
    for w in documents:
        for word in w[0]:
            all_words.append(word)
    word_lists.clear()
    word_lists['words'] = all_words
    all_words = nltk.FreqDist(all_words)
    word_features = list(all_words.keys())
    word_lists.close()
    def find_features(document):
        words = set(document)
        features = {}
        for w in word_features:
            features[w] = (w in words)
        return features

    feature_sets = [(find_features(i[0]), i[-1]) for i in documents]
    return feature_sets
