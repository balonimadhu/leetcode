class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=0
        for letter in s[::-1]:
            if letter ==" ":
                if res>=1:
                    return res
            else:
                res+=1
        return res
        