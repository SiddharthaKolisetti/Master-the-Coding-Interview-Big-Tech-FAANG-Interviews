class Solution:
    def twoSum(self, nums, target):
        numsmap = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in numsmap:
                return numsmap[nums[i]], i
            else:
                j = target - nums[i]
                numsmap[j] = i
        return None

nums = [1, 3, 7, 9, 2]
target = 11

x = Solution()
y = x.twoSum(nums, target)
print(y)
