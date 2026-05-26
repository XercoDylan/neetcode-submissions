class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += f"?{len(string)}?{string}" 

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        current_index = 0
        while (current_index < len(s) - 1):
            if s[current_index] == "?":
                for i in range(current_index + 1, len(s)):
                    if s[i] == "?":
                        length = int(s[current_index + 1:i])
                        decoded_list.append(s[i + 1: i + 1 + length])
                        current_index = i + 1 + length
                        break

        
        return decoded_list
