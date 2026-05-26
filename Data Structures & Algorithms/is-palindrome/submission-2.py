class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        backwards = ""

        for i in range(len(s)):
            if s[i].isalnum():
                forward += s[i].lower()

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                backwards += s[i].lower()

        return backwards == forward


