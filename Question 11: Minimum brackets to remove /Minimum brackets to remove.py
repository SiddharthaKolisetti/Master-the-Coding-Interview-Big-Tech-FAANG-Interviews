class Solution:
    def minRemoveToMakeValid(self, s):
        res = list(s)
        stack = []
        for i in range(len(res)):
            if res[i] == '(':
                stack.append(i)
            elif res[i] == ')' and len(stack):
                stack.pop()
            elif res[i] == ')':
                res[i] = ''
        while len(stack):
            current_index = stack.pop()
            res[current_index] = ''
        return ''.join(res)

x = Solution()
x1 = x.minRemoveToMakeValid("lee(t(c)o)de)")
print(x1)
