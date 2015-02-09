frequent_set = set(['A', 'B', 'C'])
non_frequent_set = set(['B', 'C', 'D', 'E'])

set1 = set(['A', 'B', 'C', 'D'])
set2 = set(['C', 'D', 'E'])
set3 = set(['A', 'B', 'C', 'D', 'E'])
set4 = set(['B', 'F', 'C'])

test_sets = [set1, set2, set3, set4]


def is_frequent(test_set, frequent_set, non_frequent_set):
    if test_set.issubset(frequent_set):
        print '{} is frequent'.format(sorted(test_set))
    elif non_frequent_set.issubset(test_set):
        print '{} is not frequent'.format(sorted(test_set))
    else:
        print '{} can be frequent or not frequent'.format(sorted(test_set))

for test_set in test_sets:
    is_frequent(test_set, frequent_set, non_frequent_set)
