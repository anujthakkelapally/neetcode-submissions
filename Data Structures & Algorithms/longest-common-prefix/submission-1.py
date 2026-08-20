class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str_len = len(min(strs, key=len))
        prefix = ""

        def same(iterable) -> bool:
            return len(set(iterable)) <= 1

        for index in range(shortest_str_len):
            if same(zip([string[index] for string in strs])):
                prefix += strs[0][index]
            else:
                break
        
        return prefix