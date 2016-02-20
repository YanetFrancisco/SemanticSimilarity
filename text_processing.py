from os.path import join
from re import findall
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, regexp_tokenize
import nltk
import metrics
from time import time
from nltk.corpus import wordnet
from nltk.probability import FreqDist
from collections import Counter


def text_pre_processing(file):
    with open(join(file)) as opened:
        words = set(findall('[a-z]+', opened.read()))
        english_stops = set(stopwords.words('english'))
        words = [word for word in words if word not in english_stops]
        stemmer = PorterStemmer()
        words = [stemmer.stem(word) for word in words]
        return words


def part_of_speech(tokens):
    return [(word, choose_tag(word)) for word in tokens]


def choose_tag(word):
    l = []
    for syn in wordnet.synsets(word):
        l.append(str(syn.pos()))
    if len(l) > 0:
        counter = Counter(l)
        return counter.most_common(n=1)[0][0]
    else:
        return 'no existe'


def join_dict(tags):
    classification = {'n': [], 'a': [], 'r': [], 'v': []}
    for tag in tags:
        t = tag[1]
        if t == 'n':
            classification['n'].append(tag[0])
        elif t == 'a':
            classification['a'].append(tag[0])
        elif t == 'r':
            classification['r'].append(tag[0])
        elif t == 'v':
            classification['v'].append(tag[0])
    return classification


def preprocessing_and_classification(file):
    return join_dict(part_of_speech(text_pre_processing(file)))


def sintactic_similarity(t1, t2, f):
    words_t1 = text_pre_processing(t1)
    words_t2 = text_pre_processing(t2)
    sim = 0
    for w1 in words_t1:
        min_w1 = float('+inf')
        for w2 in words_t2:
            s = f(w1, w2)
            if s < min_w1:
                min_w1 = s
        sim += min_w1
    return sim


def sintactic_similarity_with_class(t1, t2, f):
    words_t1 = preprocessing_and_classification(t1)
    words_t2 = preprocessing_and_classification(t2)
    sim = 0
    for c, words1 in words_t1.items():
        for w1 in words1:
            min_w1 = float('+inf')
            for w2 in words_t2[c]:
                s = f(w1, w2)
                if s < min_w1:
                    min_w1 = s
            sim += min_w1
    return sim


def semantic_similarity(t1, t2):
    words_t1 = preprocessing_and_classification(t1)
    words_t2 = preprocessing_and_classification(t2)
    count_words_t1 = 0
    sim = 0
    for c, words1 in words_t1.items():
        count_words_t1 += len(words1)
        if len(words_t2[c]) == 0:
            sim += len(words1)
            continue
        for w1 in words1:
            min_w1 = float('+inf')
            for w2 in words_t2[c]:
                s = metrics.wordnet_distance(w1, w2, c)
                if s < min_w1:
                    min_w1 = s
            sim += min_w1
    return sim / count_words_t1


# t = time()
# print('hamming_distance: ' + str(sintactic_similarity_with_class('cv001_18431_pos.txt', 'cv000_29590_pos.txt', metrics.hamming_distance)))
# print(time() - t)
#
# t = time()
# print('binary_distance: ' + str(sintactic_similarity_with_class('cv001_18431_pos.txt', 'cv000_29590_pos.txt', metrics.binary_distance)))
# print(time() - t)
#
# t = time()
# print('jaccard_distance: ' + str(sintactic_similarity_with_class('cv001_18431_pos.txt', 'cv000_29590_pos.txt', metrics.jaccard_distance)))
# print(time() - t)
#
# t = time()
# print('levenshtein_distance: ' + str(sintactic_similarity_with_class('cv001_18431_pos.txt', 'cv000_29590_pos.txt', metrics.levenshtein_distance)))
# print(time() - t)
#
# t = time()
# print('masi_distance: ' + str(sintactic_similarity('cv001_18431_pos.txt', 'cv000_29590_pos.txt', metrics.masi_distance)))
# print(time() - t)
#
# t = time()
# print('wordnet_distance: ' + str(semantic_similarity('cv001_18431_pos.txt', 'cv000_29590_pos.txt')))
# print(time() - t)