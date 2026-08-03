class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxi = 0
        i = 0; j = n - 1
        while i<j:
            water = (j-i) * min(heights[i], heights[j])
            if water > maxi: maxi = water

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxi