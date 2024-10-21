import re
class Solution:
    def validPalindrome(self, s):
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        n = len(s)
        l = 0
        r = len(s) - 1
        rev = s[::-1]
        if n < 2:
            return True
        if s == rev:
            return True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            if s[l] != s[r]:
                s1 = s[:l] + s[l+1:]
                s2 = s[:r] + s[r+1:]
                s3 = s1[::-1]
                s4 = s2[::-1]
                if s1 == s3 or s2 == s4:
                    return True
                else:
                    return False
        
s = 'abccdba'
x1 = Solution()
x2 = x1.validPalindrome(s)
print(x2)
