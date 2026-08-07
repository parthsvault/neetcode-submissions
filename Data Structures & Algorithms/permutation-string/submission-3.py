class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = count.get(i, 0) + 1
        print(count)
        l = 0
        r = 0
        while r < len(s2):
            if s2[r] in count and count[s2[r]] > 0:
                count[s2[r]] -= 1
                if set(count.values()) == {0}:
                    return(True)
            else:
                while l < r:
                    if s2[l] in s1:
                        count[s2[l]] += 1
                        l += 1
                        r -= 1
                        break
                    l += 1
            r += 1

        return(False)