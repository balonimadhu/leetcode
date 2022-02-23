class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
           return False
        rev=0
        value=x
        while(value>0):
            rem=value%10
            value=value//10
            rev=rev*10+rem
        return rev==x