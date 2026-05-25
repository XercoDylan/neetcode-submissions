class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in range(len(s)):
            if (s[i].lower() in alphabet):
                clean_string += s[i].lower()

        return clean_string == clean_string[::-1]
