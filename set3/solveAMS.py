from collections import Counter
import numpy as np


def compute_surpise(stream):
    occurences = Counter(stream)
    surpise = 0
    for key, value in occurences.iteritems():
        surpise += value**2
    return surpise


def ams_variables(stream, starts, length):
    variables = {}
    for start in starts:
        variables[stream[start-1]] = 0
        for i in range(start-1, length):
            if stream[i] == stream[start-1]:
                variables[stream[start-1]] += 1

    return variables


def list_median(lst):
    return np.median(np.array(lst))


def variables_median(variables):
    l = variables.values()
    return list_median(l)


def estimate_surprise(median, length):
    return length*(2*median - 1)

starts = [[9, 50, 68], [4, 31, 72], [3, 45, 72], [20, 49, 53]]
stream = [(x % 10) + 1 for x in range(0, 75)]
exact_surprise =  compute_surpise(stream)

for start in starts:
    print '----------------------------'
    print 'random starts {}'.format(start)
    variables = ams_variables(stream, start, 75)
    print 'variables {}'.format(variables)
    median = variables_median(variables)
    print 'median {}'.format(median)
    surprise = estimate_surprise(median, 75)
    print 'surpise {}'.format(surprise)
    diff = abs(surprise - exact_surprise)
    print 'diff {}'.format(diff)





