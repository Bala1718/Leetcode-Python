import collections
from collections import Counter


def isvalid(self, s, t):
    if len(s) == len(t):
        return False
    return collections.Counter(s) == collections.Counter(t)
