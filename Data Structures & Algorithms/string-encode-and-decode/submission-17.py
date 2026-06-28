class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strings = []

        for string in strs:
            encoded_strings.append("?" +  str(len(str(len(string)))) + str(len(string)) + string)

        return "".join(encoded_strings)

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        current_index = 0

        while (current_index <= len(s) - 1):
            if s[current_index] == "?":
                string_length_length = int(s[current_index + 1])

                start_index = current_index + 2 + string_length_length


                string_length = int(s[current_index + 2: current_index + 2 + string_length_length])
                end_index = start_index + string_length


                decoded_list.append(s[start_index : end_index])
                current_index = end_index
        
        return decoded_list
