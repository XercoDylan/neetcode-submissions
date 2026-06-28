class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += "?" +  str(len(str(len(string)))) + str(len(string)) + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        while (len(s) > 0):
            if s[0] == "?":
                start_index = 2 + int(s[1])
                end_index = start_index + int(s[2: 2 + int(s[1])])
                decoded_list.append(s[start_index : end_index])
                s = s[end_index:]
        
        return decoded_list
