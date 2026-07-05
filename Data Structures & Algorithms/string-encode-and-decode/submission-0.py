class Solution:

    def encode(self, strs: List[str]) -> str:

        out = ''
        for i in strs:
            out = out + i + "^_^"

        return out

    def decode(self, s: str) -> List[str]:

        org = []
        temp = ''
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i:i+3] == "^_^":
                org.append(temp)
                temp = ""
                i += 3
            else:
                temp += s[i]
                i += 1

        return org
