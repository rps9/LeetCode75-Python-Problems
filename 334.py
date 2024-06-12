class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Set the i and j values to infinity
        i = float('inf')
        j = float('inf')
        
        for num in nums:
            # If it is smaller or equal to the first than the first then it will be set to first
            if num <= i:
                i = num  
            # Only gets here if it is larger than the first 
            elif num <= j:
                j = num 
            # If it gets to here then that means it is larger than both i and j and is in order 
            else:
                return True
        
        # If nothing is found then return false
        return False
