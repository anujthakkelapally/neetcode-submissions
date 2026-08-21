class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import string
        letter_count = {letter: 0 for letter in string.ascii_lowercase}
        for letter in s:
            letter_count[letter] += 1
        for letter in t:
            letter_count[letter] -= 1
        
        for letter, count in letter_count.items():
            if count != 0:
                return False
        return True
