from collections import Counter
from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) # check if strs the same # of each letter