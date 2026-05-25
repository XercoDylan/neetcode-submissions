class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []

        def get_identifier(string: str):
            identifiers = [0] * 26

            for letter in string:
                identifiers[ord(letter)%ord("a")] += 1

            return tuple(identifiers)

        
        string_identifiers = {}

        for word in strs:
            identifier = get_identifier(word)

            if not identifier in string_identifiers:
                string_identifiers[identifier] = []

            string_identifiers[identifier].append(word) 

        for identifiers, strings in string_identifiers.items():
            output.append(strings)

        return output




        
        