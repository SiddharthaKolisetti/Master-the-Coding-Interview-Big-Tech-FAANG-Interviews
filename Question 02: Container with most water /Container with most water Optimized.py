class Solution:
    def maxArea(self, height):
        maxarea = 0
        n = len(height)
        a = 0
        b = n-1
        if n < 2:
            return "Need at least two numbers in the array"
        else:
            while a < b:
                length = min(height[a], height[b])
                width = b - a
                area = length * width
                maxarea = max(maxarea, area)
                if height[a] <= height [b]:
                    a += 1
                else:
                    b -=1  

        return maxarea

height = [1,8,6,2,5,4,8,3,7]
x = Solution()
x1 = x.maxArea(height)
print(x1)
