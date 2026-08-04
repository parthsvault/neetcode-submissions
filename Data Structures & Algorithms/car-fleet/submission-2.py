class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        for i in range(len(position)):
            stack.append([position[i], speed[i]])

        stack.sort(key = lambda x : x[0], reverse = True)

        fleets = 0

        for i in range(len(position)):
            stack[i][1] = (target - stack[i][0]) / stack[i][1]

        s = []
        for i in stack:
            if not s or i[1] > s[-1]:
                s.append(i[1])

        return len(s)
