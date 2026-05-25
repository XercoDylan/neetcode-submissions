class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def get_identifiers(string: str):
            identifier = [0] * 26
            for letter in string:
                identifier[ord(letter)%ord("a")] += 1

            return tuple(identifier)

        
        return get_identifiers(s) == get_identifiers(t)


        