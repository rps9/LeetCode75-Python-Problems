class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        # Create variables for iteration and define result as a string
        
        result = ''
        i = 0
        j = 0

        # Switch off between adding words from word1 and word2 until there is nothing left in either one
        
        while i < len(word1) and j < len(word2):
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1

        # If there are characters left in either string add them to the end until there is nothing left
      
        while i < len(word1):
            result += word1[i]
            i += 1

        while j < len(word2):
            result += word2[j]
            j += 1

        return result
