class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from math import prod
        product = 1
        output = []
        if nums.count(0) > 1:
            return [0] * len(nums)

        if nums.count(0) == 1:
            for i in nums:
                if i != 0:
                    output.append(0)
                else:
                    for i in nums:
                        if i!=0:
                            product *= i
                    output.append(product)
            return output

        for i in nums:
            product *= i 
        
        
        for i in nums:
            output.append(int(product/i))

        return output