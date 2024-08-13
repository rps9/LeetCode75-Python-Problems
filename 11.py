class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Keep track of the largest area of water and create two pointers
        max_water = 0
        j = len(height) - 1
        i = 0

        # Use the two pointers to go through the array and move it in a way that keeps it on the tallest height
        while i < j:
            water = min(height[j], height[i]) * abs(i - j)
            if water > max_water:
                max_water = water
            if height[j] < height[i]:
                j = j - 1
            else:
                i = i + 1
                

        return max_water
