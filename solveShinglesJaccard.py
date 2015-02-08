from fractions import Fraction
import math

firstWord = 'ABRACADABRA'
secondWord = 'BRICABRAC'

firstShingles = set()


def word_to_shingles(word, length=2):
    shingles = set()
    splitedWord = [word[i:i+length] for i in range(0, len(word)-1, 1)]
    for chars in splitedWord:
        shingles.add(chars)
    return shingles


def compute_jaccard_index(set_1, set_2):
    n = len(set_1.intersection(set_2))
    return Fraction(n, (len(set_1)+len(set_2)-n))

firstSet = word_to_shingles(firstWord)
secondSet = word_to_shingles(secondWord)
print '2shingles in {} :{} :{}'.format(firstWord, len(firstSet), firstSet)
print '2shingles in {} :{} :{}'.format(secondWord, len(secondSet), secondSet)
intersection = firstSet.intersection(secondSet)
print 'in common: {} total: {}'.format(intersection, len(intersection))
jaccard = compute_jaccard_index(firstSet, secondSet)
print jaccard