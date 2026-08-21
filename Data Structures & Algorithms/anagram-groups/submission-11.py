class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        anagrams = defaultdict(list)
        for string in strs:
            count = Counter(string)
            anagrams[frozenset(count.items())].append(string)
        return list(anagrams.values())
