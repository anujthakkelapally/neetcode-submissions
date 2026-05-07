class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_string_counter(string: str) -> dict[str, int]:
            string_counter = {}
            if string == "":
                return string_counter
            for letter in string:
                if letter not in string_counter:
                    string_counter[letter] = 0
                string_counter[letter] += 1
            return string_counter
        return get_string_counter(s) == get_string_counter(t)

