class Solution:
    def isValid(self, s: str) -> bool:

        opening = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        closing = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for string in s:
            if string in opening:
                stack.append(string)
            else:
                if len(stack) > 0 and stack[-1] == closing[string]:
                    stack.pop()
                else:
                    return False

        if len(stack) > 0:
            return False


        return True



