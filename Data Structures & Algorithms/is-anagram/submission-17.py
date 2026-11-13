class Solution:
    def getOrd(self, s: str):
        order = [0 for i in range(26)]

        for string in s:
            order[ord(string)%ord("a")] += 1
        

        return order

    def isAnagram(self, s: str, t: str) -> bool:
        return self.getOrd(s) == self.getOrd(t)

        