class Solution:
    def searchRange(self, nums, target):
        l1 = []
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1 and target == nums[0]:
            return [0,0]
        else:
            for i in range(len(nums)):
                if target == nums[i]:
                    l1.append(i)
            if len(l1) == 0:
                return [-1, -1]
            else:
                return [l1[0], l1[-1]]
