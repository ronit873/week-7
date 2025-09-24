class Solution:
    def reverseexponentiation(self, n):
        rev=0
        temp=n
         
        while n!=0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        return pow(temp,rev)