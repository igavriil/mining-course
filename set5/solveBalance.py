from random import randint
import copy


def balance(queries, advertisers):
    advertisers = copy.deepcopy(advertisers)
    for query in queries:
        bidded_on = [x for x in advertisers.keys() if query in advertisers[x]['bids'] and advertisers[x]['balance'] > 0]
        if len(bidded_on) == 0:
            break
        pick_advertiser = randint(0, len(bidded_on) - 1)
        advertisers[bidded_on[pick_advertiser]]['balance'] -= 1
        print query, bidded_on, pick_advertiser, bidded_on[pick_advertiser]

A = {'bids': ['x', 'y'], 'balance': 2}
B = {'bids': ['x', 'z'], 'balance': 2}
advertisers = {1: A, 2: B}

sequences = ['xzzx', 'yyxx', 'xyyz', 'zxyy']
for queries in sequences:
    print '----{}----'.format(queries)
    balance(queries, advertisers)
