class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ans = []

        for c, val in enumerate(numbers):

            if target - val in numbers:
                ans = [c + 1, numbers.index(target -val, c +1) + 1]
                return ans

            