class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n <=1:
            return n
        l = 0
        longest = 0
        seen_chars = {}
        r = 0
        for r in range(n):
            currentchar = s[r]
            prevseenchar = seen_chars.get(currentchar, -1)
            if prevseenchar >= l:
                l = prevseenchar + 1
            
            seen_chars[currentchar] = r
            longest = max(longest, r-l+1)
        return longest
        
a1 = Solution() 
a2 = a1.lengthOfLongestSubstring('abcbdca')
print(a2)
