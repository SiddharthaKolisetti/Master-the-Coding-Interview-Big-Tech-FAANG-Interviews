class Solution:
    def maxArea(self, height):
        maxarea = 0
        n = len(height)
        if n < 2:
            return "Need at least two numbers in the array"
        else:
            for i in range(n):
                for j in range(i+1, n):
                    length = min(height[i], height[j])
                    width = j - i
                    area = length * width
                    maxarea = max(maxarea, area) 
            
        return maxarea

height = [1,8,6,2,5,4,8,3,7]
x = Solution()
x1 = x.maxArea(height)
print(x1)
