class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for i in range(len(position)):
            stack.append([position[i], (target - position[i]) / speed[i]])

        stack.sort(key = lambda x : x[0], reverse = True)

        fleet = 0
        curr = 0
        for i in stack:
            if not curr or i[1] > curr:
                curr = i[1]
                fleet += 1   

        return fleet
        