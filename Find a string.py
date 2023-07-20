def count_substring(string, sub_string):
    n = 0
    pos = 0
    while True:
        try:
            pos = string.index(sub_string, pos) + 1
        except ValueError:
            return n
        n += 1
