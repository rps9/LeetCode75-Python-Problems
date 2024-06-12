class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Use dynamic programming to build off of previous solutions, create left and right products
        length = len(nums)
        left = [1] * length
        right = [1] * length
        result = []

        # Calculate the all right products using dynamic programming 
        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]

        # Calculate all left products using dynamic programming 
        for i in range(length-2 , -1, -1):
            right[i] = nums[i+1] * right[i+1]

        # Calculate the combined product to get the final answer
        for i in range(0, length):
            result.append(right[i]*left[i])

        return result   
