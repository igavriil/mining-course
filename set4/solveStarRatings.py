import numpy as np


def normalize_rows(ratings):
    rowcount, columncount = ratings.shape
    rows = np.vsplit(ratings, rowcount)
    means = np.array([avg.mean() for avg in rows])
    means = means.reshape(rowcount, 1)
    print means
    ratings = np.subtract(ratings, means)
    return ratings


def normalize_columns(ratings):
    rowcount, columncount = ratings.shape
    columns = np.hsplit(ratings, columncount)
    means = np.array([avg.mean() for avg in columns])
    means = means.reshape(1, columncount)
    print means
    ratings = np.subtract(ratings, means)
    return ratings

ratings = np.array([[1, 2, 3, 4, 5], [2, 3, 2, 5, 3], [5, 5, 5, 3, 2]])
print ratings
ratings = normalize_rows(ratings)
print ratings
ratings = normalize_columns(ratings)
print ratings
print 'min is on {} with value{}'.format(np.where(ratings == ratings.min()), ratings.min())
print 'max is on {} with value{}'.format(np.where(ratings == ratings.max()), ratings.max())
