class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
                if i == '+':
                    stack.append(stack.pop() + stack.pop())
                elif i == '-':  
                    stack.append(-stack.pop() + stack.pop())
                elif i == '/':
                    a = stack.pop()
                    stack.append(int(stack.pop() / a))
                elif i == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                     stack.append(int(i))

        return stack.pop()