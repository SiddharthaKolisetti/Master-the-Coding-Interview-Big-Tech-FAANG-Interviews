import re
class Solution:
    def isPalindrome(self, s):
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        s1 = s[::-1]
        if s == s1:
            return True
        else:
            return False
s = 'A man'
x1 = Solution()
x2 = x1.isPalindrome(s)
print(x2)
