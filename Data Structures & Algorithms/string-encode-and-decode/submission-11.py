class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string = encoded_string + "#" + str(len(string)) + "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        while (len(s) > 0):
            for i in range(1, len(s)):
                if s[i] == "#":
                    string_length = int(s[1:i])
                    decoded_list.append(s[i + 1: i + 1 + string_length])
                    s = s[i + 1 + string_length:]
                    break

        return decoded_list
