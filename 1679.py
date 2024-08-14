class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Sort the array to prepare for the two pointer approach
        nums.sort()

        # Initialize indexes and running total
        i = 0
        j = len(nums) - 1
        total_combo = 0

        # Go through the array in a way that always tries to move you towards the correct answer and keep count
        while i < j:
            if nums[i] + nums[j] == k:
                total_combo += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        
        return total_combo

        
