class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def fingerprint(word: str) -> tuple(int):
            import string
            fp = [0 for _ in range(len(string.ascii_lowercase))]
            for letter in word:
                fp[ord(letter)-ord('a')] += 1
            return tuple(fp)

        anagram_map = defaultdict(list)
        for word in strs:
            fp = fingerprint(word)
            anagram_map[fp].append(word)
        return list(anagram_map.values())

