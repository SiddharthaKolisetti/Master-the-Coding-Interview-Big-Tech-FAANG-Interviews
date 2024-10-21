class Solution:
    def BS(self, nums, left, right, target):
        while left <= right:
            mid = int((left + right) / 2)
            key = nums[mid]
            if key == target:
                return mid
            elif key < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1 and target == nums[0]:
            return [0,0]
        firstpos = self.BS(nums, 0, len(nums) - 1, target)
        if firstpos == -1:
            return [-1, -1]
        startpos = firstpos
        endpos = firstpos
        while startpos != -1:
            temp1 = startpos
            startpos = self.BS(nums, 0, startpos - 1, target)
        startpos = temp1
        while endpos != -1:
            temp2 = endpos
            endpos = self.BS(nums, endpos + 1, len(nums) - 1, target)
        endpos = temp2
        return [startpos, endpos]
