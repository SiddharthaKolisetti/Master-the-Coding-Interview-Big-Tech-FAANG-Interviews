class Solution:
    def trap(self, height):
        n = len(height)
        total = 0
        for i in range(n):
            leftp = i
            rightp = i
            maxL = 0
            maxR = 0
            while leftp >= 0:
                maxL = max(maxL, height[leftp])
                leftp -= 1
            while rightp < n:
                maxR = max(maxR, height[rightp])
                rightp +=1
            current_water = min(maxL, maxR) - height[i]
            if current_water >= 0:
                total += current_water
        return total

height = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
x = Solution()
y = x.trap(height)
print(y)
