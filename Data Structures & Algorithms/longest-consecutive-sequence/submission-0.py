class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(nums)
        i = 0; seq = 0; m = 0
        l = 0
        while True:
            if l >= len(nums):
                return m

            if nums[l] + i in nums:
                seq += 1 
                i += 1
            else:
                l += 1
                i = 0
                if m < seq: m = seq 
                seq = 0

            