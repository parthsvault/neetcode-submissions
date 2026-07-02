class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        

        def counter(inp):
            count = {}
            for char in inp:
                count[char] = count.get(char, 0) + 1
           
            return count

        s_map = counter(s)
        t_map = counter(t)

        if s_map == t_map: return True 
        else: return False