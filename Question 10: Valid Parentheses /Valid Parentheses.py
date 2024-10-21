class Solution:
    def isValid(self, s):
        s1 = []
        hashmap = {'(' : ')', '{' : '}',  '[' : ']'}
        n = len(s)
        for i in range(n):
            if s[i] in hashmap:
                s1.append(s[i])
            elif not s1 or hashmap[s1.pop()] != s[i]:
                return False
        return len(s1) == 0
