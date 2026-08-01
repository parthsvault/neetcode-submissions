class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2:
            return False

        stack = []
        for i in s:

            if i in '{([':
                stack.append(i)
            
            elif not stack:
                return False
            else:
                top  = stack.pop()
                if i == ')' and top != '(' : return False
                if i == ']' and top != '[' : return False
                if i == '}' and top != '{' : return False

        return not stack

            