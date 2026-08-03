class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, p in enumerate(nums):
            left = i+1
            right = len(nums) - 1 
            
            while left < right:
                sum = nums[right] + nums[left]
                if -p == sum:
                    ans.append([p, nums[right], nums[left]])
                    left += 1
                    right -= 1

                if -p < sum:
                    right -= 1
                if -p > sum:
                    left +=1

        t = set(tuple(items) for items in ans)
        ans = list(items for items in t)

        return ans