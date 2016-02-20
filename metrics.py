def jaccard_distance(word1, word2):
    list1 = [w for w in word1]
    list2 = [w for w in word2]
    set1 = set(list1)
    set2 = set(list2)
    return float(len(set1.union(set2)) - len(set1.intersection(set2))) / len(set1.union(set2))


def n_gramas_distance(word1, word2):
    pass


def init_matrix(len1, len2):
    m = []
    for i in range(len1):
        m.append([0] * len2)
    for i in range(len1):
        m[i][0] = i
    for j in range(len2):
        m[0][j] = j
    return m


def levenshtein_distance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    m = init_matrix(len1 + 1, len2 + 1)
    for i in range(len1):
        for j in range(len2):
            m[i + 1][j + 1] = min((m[i][j + 1] + 1), (m[i][j] + (word1[i] != word2[j])), (m[i + 1][j] + 1))
    return m[len1][len2]


def binary_distance(word1, word2):
    if word1 == word2:
        return 0.0
    else:
        return 1.0


def aux_hamming_distance(menor, mayor, dif):
    new_word = menor + dif * '*'
    distancia = 0
    for w in range(len(new_word)):
        if new_word[w] != mayor[w]:
            distancia += 1
    return distancia


def hamming_distance(word1, word2):
    dif = len(word1) - len(word2)
    return aux_hamming_distance(word1, word2, abs(dif)) if dif <= 0 else aux_hamming_distance(word2, word1, abs(dif))


def masi_distance(word1, word2):
    list1 = [w for w in word1]
    list2 = [w for w in word2]
    set1 = set(list1)
    set2 = set(list2)
    return 1 - float(len(set1.intersection(set2))) / max(len(set1), len(set2))


from nltk.corpus import wordnet
def wordnet_distance(word1, word2, tag1):
    w1 = wordnet.synsets(word1, pos=tag1)[0]
    w2 = wordnet.synsets(word2, pos=tag1)[0]
    s = w1.wup_similarity(w2)
    if s is None:
        return 1
    return 1 - s


#surgical = len(wordnet.synsets('surgical', pos='a'))
#print(surgical)
#fantastic = wordnet.synsets('fantastic')
#print(fantastic)
#sim = surgical.wup_similarity(fantastic)
#print(sim)

from nltk.metrics import distance
# w1 = set(['r', 'a', 'i', 'n'])
# w2 = set(['t', 'r', 'a', 'i', 'n'])
# print(jaccard_distance('train', 'rain'))
# print(w1.union(w2))
# print(w1.intersection(w2))
# print(3 * 'a')
#print(levenshtein_distance('shine', 'rain'))
#print(masi_distance('rain', 'rain'))
#print(distance.edit_distance('distorsion', 'distancia'))
#print(masi_distance('synopsis', 'mentally'))


