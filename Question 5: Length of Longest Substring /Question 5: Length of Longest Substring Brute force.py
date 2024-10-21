class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n <=1:
            return n
        longest = 0
        for i in range(n):
            seen_chars = {}
            currentLength = 0
            for j in range(i,n):
                currentchar = s[j]
                if currentchar not in seen_chars:
                    currentLength +=1
                    seen_chars[currentchar] = True
                    longest = max(longest, currentLength)
                else:
                    break
        return longest

a1 = Solution() 
a2 = a1.lengthOfLongestSubstring('abcbdca')
print(a2)
