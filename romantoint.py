class Solution:
    def romanToInt(self, s: str) -> int:
        d={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        prev='I'
        result=0
        curr=0
        for curr in s[::-1]:
            if(d[curr]<d[prev]):
                result = result-d[curr]
            else:
                result = result+d[curr]
            prev=curr
        return result
    