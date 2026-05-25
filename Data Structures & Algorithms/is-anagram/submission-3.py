class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
        
        for char in t:
            if not (char in characters):
                return False
            characters[char] -= 1

            if characters[char] <= 0:
                del characters[char]
        
        return True
        