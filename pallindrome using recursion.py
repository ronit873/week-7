class Solution:
    def isPalindrome(self, n):
        return True if n == int(str(n)[::-1]) else False