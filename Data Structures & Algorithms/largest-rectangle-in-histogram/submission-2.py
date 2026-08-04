class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        for ind, height in enumerate(heights):
            start = ind
            while stack and height < stack[-1][1]:
                start_i, h = stack.pop()
                maxArea = max(maxArea, (ind - start_i) * h)
                start = start_i 

            stack.append((start, height))

        while stack:
            start, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - start) * h)
      
        return maxArea