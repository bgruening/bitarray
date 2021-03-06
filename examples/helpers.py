from bitarray import bitarray


def trim(a):
    "return a bitarray, with zero bits removed from beginning"
    try:
        first = a.index(1)
    except ValueError:
        return bitarray()
    last = len(a) - 1
    while not a[last]:
        last -= 1
    return a[first:last+1]

def find_last(a, value=True):
    "find the last occurrence of value, in bitarray."
    i = len(a) - 1
    while not a[i] == bool(value):
        i -= 1
    return i

def count_n(a, n):
    "return the index i for which a[:i].count() == n"
    i, j = n, a.count(1, 0, n)
    while j < n:
        if a[i]:
            j += 1
        i += 1
    return i

if __name__ == '__main__':
    # trim
    assert trim(bitarray()) == bitarray()
    assert trim(bitarray('000')) == bitarray()
    assert trim(bitarray('111')) == bitarray('111')
    assert trim(bitarray('00010100')) == bitarray('101')

    # find_last
    assert find_last(bitarray('00010100')) == 5
    assert find_last(bitarray('00010111'), 0) == 4
    assert find_last(bitarray('0000'), 0) == 3

    # count_n
    a = bitarray('11111011111011111011111001111011111011111011111010111010111')
    for n in range(0, 48):
        i = count_n(a, n)
        assert a[:i].count() == n
