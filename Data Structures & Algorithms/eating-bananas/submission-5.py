class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            hrs = 0
            for i in piles:
                hrs += -(-i // mid)
            if hrs <= h:
                ans = mid
                r = mid - 1
            elif hrs > h:
                l = mid + 1

        return ans
