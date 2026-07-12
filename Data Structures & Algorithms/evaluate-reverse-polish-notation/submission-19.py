class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        operands = []

        for token in tokens:
            if token in operators:
                num1 = operands.pop()
                num2 = operands.pop()

                if token == '+':
                    result = num2 + num1
                elif token == '-':
                    result = num2 - num1
                elif token == "*":
                    result = num2 * num1
                elif token == "/":
                    result = int(num2 / num1)
                
                operands.append(result)
            else:
                operands.append(int(token))

        
        return operands[-1]

        