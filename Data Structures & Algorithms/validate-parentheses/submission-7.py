class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for string in s:
            if string in ("(","{","["):
                stack.append(string)
            else:
                if len(stack) == 0:
                    return False 
                    
                if not (stack[-1] == closing[string]):
                    return False
                else:
                    stack.pop(-1)

        
        if len(stack) > 0:
            return False
        else:
            return True

        