class Solution:
    def backspaceCompare(self, s, t):
        def process_string(string):
            processed = []
            for char in string:
                if char != '#':
                    processed.append(char)
                elif processed:  # Check if the processed list is not empty
                    processed.pop()
            return ''.join(processed)

        return process_string(s) == process_string(t)

S = 'x#y'
T = 'b#'
x1 = Solution()
x2 = x1.backspaceCompare(S, T)
print(x2)
