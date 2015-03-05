from itertools import combinations

input = ['a', 'b', 'c', 'd']
sets = [set(['A', 'B']),
        set(['B', 'C']), 
        set(['C', 'D']),
        set(['D', 'E']),  
        set(['E', 'F']), 
        set(['F', 'G']), 
        set(['G', 'H']), 
        set(['A', 'H']), 
        set(['A', 'D', 'G']), 
        set(['A', 'D', 'F'])]

set_cover = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

def find_cover_set(sets, set_cover):
    for i in range(2, len(sets)+1):
        all_comb = map(list, combinations(sets, i))
        found = False
        for combination in all_comb:
            cover = set([item for subset in combination for item in subset])
            if cover == set_cover:
                found = True
                print combination, len(combination)
                print '---'
                print cover
                print '--------------------'
        if found:
            return
            
find_cover_set(sets, set_cover)

def find_simple(sets, set_cover):
    all_sets = []
    cover_set = set()
    for s in sets:
        if s - cover_set != set():
            cover_set = cover_set | s
            all_sets.append(s)
        if cover_set == set_cover:
            return len(all_sets), all_sets, cover_set

def find_dump(sets, set_cover):
    all_sets = []
    cover_set = set()
    for s in sets:
        cover_set = cover_set | s
        all_sets.append(s)
        if cover_set == set_cover:
            return len(all_sets), all_sets, cover_set




print find_simple(sets, set_cover)
print find_dump(sets, set_cover)
