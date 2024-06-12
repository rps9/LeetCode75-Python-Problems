class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        # Find the max amount of candy and create an empy vector 
        most_candy = max(candies)
        result = []

        # Append boolean values to vector checking if adding the extra candy is greater than or equal to the max
        for candy in candies:
            result.append(candy + extraCandies >= most_candy)

        # Return the resultant boolean vector 
        return result
