from test import test


def find(strng, ch):

    ix = 0
    while ix< len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
        return -1


print(find("Compsci", "p") == 3)