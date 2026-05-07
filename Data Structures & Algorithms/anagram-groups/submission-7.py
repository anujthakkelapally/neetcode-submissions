class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_anagram_id(word: str) -> tuple[int]:
            anagram_id = [0 for _ in range(26)]
            for letter in word:
                anagram_id[ord(letter) - ord('a')] += 1

            return tuple(anagram_id)
        
        anagram_dict = {}
        for word in strs:
            anagram_id = get_anagram_id(word)
            if anagram_id not in anagram_dict:
                anagram_dict[anagram_id] = []
            anagram_dict[anagram_id].append(word)
        
        return list(anagram_dict.values())