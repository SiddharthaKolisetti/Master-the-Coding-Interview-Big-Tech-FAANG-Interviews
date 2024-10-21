class Solution:
    def trap(self, height):
        n = len(height)
        total = 0
        a = 0
        b = n - 1
        maxL = 0
        maxR = 0
        while a < b:
            if height[a] <= height[b]:
                if height[a] >= maxL:
                    maxL = height[a]
                else:
                    total += maxL - height[a]
                a += 1
            else:
                if height[b] >= maxR:
                    maxR = height[b]
                else:
                    total += maxR - height[b]
                b -= 1
        return total

height = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
x = Solution()
y = x.trap(height)
print(y)
