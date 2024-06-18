class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0

        for i in range(0, len(nums)):
            if  nums[count] == 0: # If the number is zero, add it to the end of the list and remove it
                nums.pop(count)
                nums.append(0)
            else:
                count += 1
