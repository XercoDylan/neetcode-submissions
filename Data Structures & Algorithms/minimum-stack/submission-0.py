class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minimum = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])


    def pop(self) -> None:
        popped = self.stack.pop(-1)
        self.minStack.pop(-1)

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
