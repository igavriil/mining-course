import itertools


# a set with all possible items or collection of
# items in a basket
def basket_subsets(basket):
    subsets = []
    for subsetsize in range(len(basket)):
        b = set(itertools.combinations(basket, subsetsize+1))
        for subset in b:
            subsets.append(subset)
    return subsets


# a set with all posible itemsets in all baskets
def all_subsets(baskets):
    subsets = set()
    for basket in all_baskets:
        for subset in basket_subsets(basket):
            subsets.add(subset)
    return subsets


# a list with occurence count of all posible itemsets
# in the baskets
def itemsets_frequency(itemsets, baskets):
    frequency_dict = {}
    for itemset in itemsets:
        frequency_dict[str(itemset)] = 0
    for basket in baskets:
        for subset in basket_subsets(basket):
            frequency_dict[str(subset)] += 1
    return frequency_dict


def filter_by_frequency(frequency_dict, support, confidence):
    support_dict = {}
    confidence_dict = {}
    for item, frequency in frequency_dict.iteritems():
        if frequency >= support:
            support_dict[item] = frequency
        if frequency >= support*confidence:
            confidence_dict[item] = frequency
    return support_dict, confidence_dict


def print_frequency_dicts(frequency_dict):
    for item, frequency in frequency_dict.iteritems():
        print item, frequency

b1 = set(['m', 'c', 'b'])
b2 = set(['m', 'p', 'j'])
b3 = set(['m', 'b'])
b4 = set(['c', 'j'])
b5 = set(['m', 'p', 'b'])
b6 = set(['m', 'c', 'b', 'j'])
b7 = set(['c', 'b', 'j'])
b8 = set(['b', 'c'])


all_baskets = [b1, b2, b3, b4, b5, b6, b7, b8]
all_baskets_subsets = all_subsets(all_baskets)

frequencies = itemsets_frequency(all_baskets_subsets, all_baskets)
support, confidence = filter_by_frequency(frequencies, 2, 2)
print "-- support --"
print_frequency_dicts(support)
print '-- confidence --'
print_frequency_dicts(confidence)


# for key, value in test:
#     print key, value

# for basket in all_baskets:
#     for subset in basket_subsets(basket):
#         print subset
