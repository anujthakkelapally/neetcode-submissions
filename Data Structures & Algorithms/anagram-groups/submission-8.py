class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_string_id(word: str) -> tuple[int]:
            string_id = [0 for _ in range(26)]
            for letter in word:
                letter_position = ord(letter) - ord('a')
                string_id[letter_position] += 1
            return tuple(string_id)
        
        anagrams = defaultdict(list)
        for string in strs:
            string_id = get_string_id(string)
            anagrams[string_id].append(string)
        
        return list(anagrams.values())
