class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for letter in s:
            s_count[letter] += 1
        for letter in t:
            t_count[letter] += 1
        return s_count == t_count