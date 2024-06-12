class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Code is based around the idea that if there is three zeroes in a row you can place a flower and if there are 2 zeroes at the beginning or the end then you can place a flower
        # Start the count at one since the edge is like having a one zero already there 
        count = 1
        
        # Check conditions to see if you can place a flower 
        for flower in flowerbed:
            if flower == 0:
                count += 1
            if flower == 1:
                count = 0
            if count == 3:
                n -= 1
                count = 1
            if n == 0:
                return 1

        # At the end if you have two zeroes you can place one more flower
        if count == 2:
            n -= 1
        
        # Check if there are no flowers left
        return n == 0
