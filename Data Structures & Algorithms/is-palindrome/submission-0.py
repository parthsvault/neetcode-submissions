class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_s = ''
        for i in s:
            if not i.isalnum():
                continue
            else:
                strip_s += i.lower()


        for i in range(len(strip_s)//2):
            if strip_s[i] == strip_s[-i-1]:
                continue
            else:
                return False
            
        return True