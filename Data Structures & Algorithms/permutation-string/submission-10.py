class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count = {}
        for i in s1:
            count[i] = count.get(i,0) + 1
        
        match = {}
        l = 0

        for r in range(len(s2)):
            match[s2[r]] = match.get(s2[r], 0) + 1

            while r-l+1 > len(s1):
                match[s2[l]] -= 1
                if match[s2[l]] == 0:
                    del match[s2[l]]
                l += 1

            if count == match:
                return True

        return False