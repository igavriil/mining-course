from collections import defaultdict

def calclulate_prefix(jaccard_sim, string):
    p = int((1-jaccard_sim)*len(string)) + 1
    return p


s1 = "abcef"
s2 = "acdeg"
s3 = "bcdefg"
s4 = "adfg"
s5 = "bcdfgh"
s6 = "bceg"
s7 = "cdfg"
s8 = "abcd"

string_set = [s2, s3, s4, s5, s6, s7, s8]


print calclulate_prefix(0.2, s1)

to_search = set()
indexes = defaultdict(list)
for symbol in s1[:calclulate_prefix(0.2, s1)]:
    indexes[symbol].append(s1)
    for string in string_set:
        if symbol in string:
            indexes[symbol].append(string)
            to_search.update([string])

print indexes
print to_search
