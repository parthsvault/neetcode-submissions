class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        tracker = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while s and s[-1][0] < val:
                stackT, stackInd = s.pop()
                tracker[stackInd] = i - stackInd

            s.append((val, i))

        return tracker
        