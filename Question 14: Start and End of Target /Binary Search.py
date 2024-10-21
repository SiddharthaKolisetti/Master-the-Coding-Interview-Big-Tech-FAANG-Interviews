def BS(nums, target):
    l = 0
    h = len(nums) - 1
    while l<=h:
        mid = int((l+h)/2)
        key = nums[mid]
        if key == target:
            return mid
        elif key < target:
            l = mid + 1
        else:
            h = mid - 1
    return -1
x = BS([5, 6, 7, 8, 9, 10, 11], 7)
print(x)
