class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Use split method to create an list of strings and set the delimiter to nothing to remove all whitespace then reverse the list and join it using space as the joining method
        return ' '.join(list(reversed(s.split())))
