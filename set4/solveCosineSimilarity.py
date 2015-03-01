import numpy as np


def cosine_similarity(a, b, scale_factor):
    a_sc, b_sc = np.copy(a), np.copy(b)
    a_sc[-1], b_sc[-1] = scale_factor*a[-1], scale_factor*b[-1]
    return 1-(np.dot(a_sc, b_sc)/(np.linalg.norm(a_sc)*np.linalg.norm(b_sc)))


profileA = np.array([1, 0, 1, 0, 1, 2])
profileB = np.array([1, 1, 0, 0, 1, 6])
profileC = np.array([0, 1, 0, 1, 0, 2])


for scale in [0, 0.5, 1, 2]:
    ab = cosine_similarity(profileA, profileB, scale)
    ac = cosine_similarity(profileA, profileC, scale)
    print ab, ac
    if ab < ac:
        print 'for a={} A is closer to B than C'.format(scale)
    else:
        print 'for a={} A is closer to C than B'.format(scale)
