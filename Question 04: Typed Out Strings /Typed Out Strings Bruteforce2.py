class Solution:
    def backspaceCompare(self, s, t):
        S_list = buildString(s)
        T_list = buildString(t)
        if len(S_list) != len(T_list):
            return False
        else:
            for i in range(len(S_list)):
                if S_list[i] != T_list[i]:
                    return False
        return True
    
def buildString(string):
    Build_list = []
    for i in string:
        if i != '#':
            Build_list.append(i)
        if i == '#':
            if len(Build_list) != 0:
                Build_list.pop()

    return Build_list

S = 'ab#c'
T = 'ad#c'
x1 = Solution()
x2 = x1.backspaceCompare(S, T)
print(x2)
