class Solution:
    def backspaceCompare(self, s, t):
        S_list = []
        T_list = []
        for i in s:
            if i != '#':
                S_list.append(i)
            if i == '#':
                if len(S_list) != 0:
                    S_list.pop()

        for j in t:
            if j != '#':
                T_list.append(j)
            if j == '#':
                if len(T_list) != 0:
                    T_list.pop()
    
        y = listCompare(S_list, T_list)
        return y

def listCompare(S_list, T_list):
    if S_list == T_list:
        return True
    else:
        return False
        
S = 'x#y'
T = 'b#'
x1 = Solution()
x2 = x1.backspaceCompare(S, T)
print(x2)
