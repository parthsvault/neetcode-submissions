class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 0

    def push(self, val: int) -> None:
        self.stack.insert(0, val)

        if self.mini > val:
            self.mini = val

    def pop(self) -> None:
        del self.stack[0]

    def top(self) -> int:
        return self.stack[0] 
        

    def getMin(self) -> int:
        return min(self.stack)
        
