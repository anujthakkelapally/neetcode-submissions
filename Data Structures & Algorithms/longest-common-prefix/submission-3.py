class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for letters in zip(*strs):
            if len(set(letters)) == 1:
                prefix += letters[0]
            else:
                return prefix
        
        return prefix
