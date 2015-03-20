pos = [(28, 145), (38, 115), (43, 83), (50, 130), (50, 90), (50, 60), (50, 30), (55, 118), (63, 88), (65, 140)]
neg = [(23, 40), (25, 125), (29, 97), (33, 22), (35, 63), (42, 57), (44, 105), (55, 63), (55, 20), (64, 37)]

decisions = {0: [{'age': 45}], 1: [{'sal': 110}, {'sal': 75}]}

levels = len(decisions.keys())
for point in pos + neg:
    age, sal = point
    path = 0
    decision = 0
    # print '------------'
    # print '{} {} '.format(age, sal)
    for level, rules in decisions.iteritems():
        
        if rules[decision].keys()[0] == 'age':
            if age > rules[decision].values()[0]:
                decision = 1
            else:
                decision = 0
        elif rules[decision].keys()[0] == 'sal':
            if sal > rules[decision].values()[0]:
                decision = 1
            else:
                decision = 0
        path += decision*(levels - level)
        # print 'decision {}'.format(decision)
    if point in pos and (path == 0 or path == 2):
        print '{} {} '.format(age, sal)
        print 'path {}'.format(path)
        print '------------'
    if point in neg and (path == 1 or path == 3):
        print '{} {} '.format(age, sal)
        print 'path {}'.format(path)
        print '------------'

        # print rules

