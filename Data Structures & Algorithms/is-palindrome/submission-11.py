class Solution:
    def isAlphanumeric(self, s: str):
        is_lower = "a" <= s <= "z"
        is_upper = "A" <= s <= "Z"
        is_digit = "0" <= s <= "9"

        return is_lower or is_upper or is_digit


    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        while (front < back):

            while not self.isAlphanumeric(s[front]):
                front += 1
                if front > len(s) - 1:
                    return True
            
            while not self.isAlphanumeric(s[back]):
                back -= 1

                if back < 0:
                    return True

            if s[front].lower() != s[back].lower():
                return False

            front += 1
            back -= 1

        return True
        