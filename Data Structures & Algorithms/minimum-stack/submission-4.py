class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)

        if not self.mini:
            self.mini.append(val)
        else:
            self.mini.append(min(val, self.mini[-1]))

    def pop(self) -> None:
        del self.stack[0]
        self.mini.pop()

    def top(self) -> int:
        return self.stack[0] 
        

    def getMin(self) -> int:
        return self.mini[-1]
        
