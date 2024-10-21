class Solution:
    def trap(self, height):
        n = len(height)
        a = 0
        b = n-1
        total = 0
        maxL = 0
        maxR = 0
        for i in range(n):
            h1 = height[:i+1]
            h2 = height[i:n+1]
            maxL = max(h1)
            maxR = max(h2)
            current_water = min(maxL, maxR) - height[i]
            if current_water >= 0:
                total = total + current_water
            else:
                total = total + 0
        return total

height = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
x = Solution()
y = x.trap(height)
print(y)
