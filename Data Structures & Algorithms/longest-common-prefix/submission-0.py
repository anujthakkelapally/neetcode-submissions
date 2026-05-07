class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        shortest_word_len = min([len(word) for word in strs])
        prefix = ""
        for index in range(shortest_word_len):
            letter = None
            for word in strs:
                if letter and word[index] != letter:
                    return prefix
                letter = word[index]
            prefix += letter
        return prefix