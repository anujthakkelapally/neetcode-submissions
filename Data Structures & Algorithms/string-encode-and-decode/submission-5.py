class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for text in strs:
            encoded += f'{len(text)}#{text}'
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        length_str = ""
        while index < len(s):
            
            if s[index] == '#':
                length = int(length_str)
                decoded.append(s[index+1:index+1+length])
                index += length
                length_str = ""
            else:
                length_str += s[index]
            index += 1
            # 3#sky4#blow
            
        return decoded


