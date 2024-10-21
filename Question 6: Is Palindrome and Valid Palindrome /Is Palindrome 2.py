import re
class Solution:
    def isPalindrome(self, s):
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
            
        return True

s = 'Race a car'
x1 = Solution()
x2 = x1.isPalindrome(s)
print(x2)
