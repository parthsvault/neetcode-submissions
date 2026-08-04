class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        for i in range(len(position)):
            stack.append([position[i], (target - position[i]) / speed[i]])

        stack.sort(key = lambda x : x[0], reverse = True)


        s = []
        for i in stack:
            if not s or i[1] > s[-1]:
                s.append(i[1])

        return len(s)
