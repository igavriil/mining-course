def hash(element):
    value = (3 * element + 7) % 11
    return '{0:04b}'.format(value)


def tail_length(hashvalue):
    return len(hashvalue) - len(hashvalue.rstrip('0'))


def max_tail(stream):
    max_tail = 0
    for element in stream:
        if tail_length(hash(element)) > max_tail:
            max_tail = tail_length(hash(element))
    return max_tail


def print_distinct_appr(stream):
    tail = max_tail(stream)
    appr = 2**tail
    print '{}: max tail:{} estimate:{}'.format(stream, tail, appr)


streams = [[4, 5, 6, 7], [2, 5, 7, 10], [2, 6, 8, 10], [1, 3, 6, 6]]
for stream in streams:
    print_distinct_appr(stream)

