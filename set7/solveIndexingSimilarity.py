from collections import defaultdict


def calclulate_prefix(jaccard_sim, string):
    p = int(jaccard_sim*len(string) + 1)
    return p


def create_index_buckets(string_set, jaccard_sim):
    index_buckets = defaultdict(list)
    for string in string_set:
        for symbol in string[:calclulate_prefix(jaccard_sim, string)]:
            index_buckets[symbol].append(string)

    return index_buckets


def to_compare(index_buckets, probe_string, jaccard_sim):
    compare_set = set()
    for symbol in probe_string[:calclulate_prefix(jaccard_sim, probe_string)]:
        compare_set.update(index_buckets[symbol])
        compare_set.discard(probe_string)

    return compare_set

s1 = "abcef"
s2 = "acdeg"
s3 = "bcdefg"
s4 = "adfg"
s5 = "bcdfgh"
s6 = "bceg"
s7 = "cdfg"
s8 = "abcd"

string_set = [s1, s2, s3, s4, s5, s6, s7, s8]

index_buckets = create_index_buckets(string_set, 0.2)

for probe_string in [s1, s3, s6]:
    print probe_string
    compare_set = to_compare(index_buckets, probe_string, 0.2)
    print compare_set
    print len(compare_set)
