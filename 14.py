def build_bad_char_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


def my_find(string, pattern, start=0, end=None):
    if end is None:
        end = len(string)

    search_str = string[start:end]
    n = len(search_str)
    m = len(pattern)

    if m == 0:
        return start
    if m > n:
        return -1

    bad_char = build_bad_char_table(pattern)

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == search_str[i + j]:
            j -= 1
        if j == -1:
            return start + i
        else:
            bc_shift = j - bad_char.get(search_str[i + j], -1)
            i += max(1, bc_shift)

    return -1


def find_all(string, pattern):
    indices = []
    start = 0

    while True:
        pos = my_find(string, pattern, start)
        if pos == -1:
            break
        indices.append(str(pos))
        start = pos + 1

    return ",".join(indices)


dna_string = "ATCGATCGGCTATCGAATCG"
search = "ATC"

print(my_find(dna_string, search))
print(my_find(dna_string, search, 5))
print(my_find(dna_string, search, 5, 15))
print(find_all(dna_string, search))