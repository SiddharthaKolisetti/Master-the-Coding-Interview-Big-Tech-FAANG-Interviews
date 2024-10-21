import re
class Solution:
    def isPalindrome(self, s):
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        n = len(s)
        if n < 1:
            return True
        else:
            if n%2 == 0:
                mid1 = int((n/2) - 1)
                mid2 = int(n/2)
                while mid1 >= 0 and mid2 < n:
                    if s[mid1] != s[mid2]:
                        return False
                    mid1 -= 1
                    mid2 += 1
                return True
        
            elif n%2 !=0:
                mid1 = int((n-1)/2)
                mid2 = int((n-1)/2)
                while mid1 >= 0 and mid2 < n:
                    if s[mid1] != s[mid2]:
                        return False
                    mid1 -= 1
                    mid2 += 1 
                return True
        
s = 'abb'
x1 = Solution()
x2 = x1.isPalindrome(s)
print(x2)
