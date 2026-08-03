class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, 0
        l_max = [0]*n
        r_max = [0]*n

        for i in range(n):
            j = -i - 1
            l_max[i] = l
            r_max[j] = r  
            l = max(height[i], l)
            r = max(height[j],r)

        sum = 0
        for i in range(n):
            water = min(l_max[i], r_max[i]) - height[i]

            if water > 0:
                sum += water

        return sum
            