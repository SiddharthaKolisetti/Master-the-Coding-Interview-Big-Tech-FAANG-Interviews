class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        if n < 2:
            return None
        else:
            for i in range(n):
                for j in range(i+1, n):
                    if nums[i] + nums[j] == target:
                        return i, j
            return None

nums = [1, 3, 7, 9, 2]
target = 11

x = Solution()
y = x.twoSum(nums, target)
print(y)
