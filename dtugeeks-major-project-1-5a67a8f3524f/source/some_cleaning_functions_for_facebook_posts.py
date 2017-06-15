import os
import re

import ownModule
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


def rem_hash_tags(post):
    # remove all the #tags and replace them with an empty string
    post = re.sub(r"[#][a-zA-Z]+ ?", "", post, re.IGNORECASE)
    # the below if handles a small case , when we have like "Python is (#Magic)".
    # --> "Python is ", so we don't want the last space
    # whereas in other cases this if is not required like "Python is (#surely )Magic"-->"Python is Magic"
    if post:
        if post[-1] == ' ':
            return post[:-1]
    return post


def rem_links(post):
    # remove all the #tags and replace them with an empty string
    post = re.sub("https?\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*) ", "",
                  post, re.IGNORECASE)
    post = re.sub(r"https?://[.a-zA-Z0-9?&%/-]+ ?", "", post, re.IGNORECASE)
    post = re.sub(r"www.[.a-zA-Z0-9?&%]+ ?", "", post, re.IGNORECASE)
    post = re.sub("[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*) ", "", post, re.IGNORECASE)
    # the below if handles a small case , when we have like "Python is (#Magic)".
    # --> "Python is ", so we don't want the last space
    # whereas in other cases this if is not required like "Python is (#surely )Magic"-->"Python is Magic"
    if post:
        if post[-1] == ' ':
            post = post[:-1]
    return post


def remove_negative_stopwords(stop_words, remove_list):
    for word in remove_list:
        if word in stop_words:
            stop_words.remove(word)
    return stop_words


def main():
    file_folder = ownModule.getProjectRoot() + "outputFiles" + os.path.sep
    name = file_folder + "HDFC.bankFaceBookPosts.csv"

    result = ownModule.removeFileIfExists(file_folder + "Cleaned-HDFC-FBPosts" + '.txt')
    rf = open(result, "a")
    with open(name) as f:
        # Get a list of stopwords
        stop_words = list(stopwords.words('english'))
        remove_list = ['not', 'nor', 'never', 'no']
        stop_words = remove_negative_stopwords(stop_words, remove_list)
        ps = PorterStemmer()
        # read the given file
        for t in f:
            st = sent_tokenize(t)
            # for each sentence
            for sent in st:
                # remove the hashtags from this sentence
                sent = rem_hash_tags(sent)
                # remove links from this sentence
                sent = rem_links(sent)
                # tokenize into the words
                word_tokens = word_tokenize(sent)
                # remove the stop words
                filtered_sentence = [w for w in word_tokens if not w in stop_words]
                # uncomment the below line to initiate the spell spellCorrector
                # filtered_sentence=[spellCorrector.correct(w) for w in filtered_sentence]
                rf.write(' '.join(filtered_sentence))
                rf.write("\n")


if __name__ == "__main__":
    main()
