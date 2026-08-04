class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        while len(nums) > 1:
            n = len(nums) // 2
            if nums[n] <= target:
                nums = nums[n:]
                index += n

            else:
                nums = nums[:n]


        return index if target == nums[0] else -1