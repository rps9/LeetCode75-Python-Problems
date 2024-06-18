class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Define variables used
        i = 0

        # Check conditions where you can return right away
        if len(s) > len(t):
            return False
        elif len(s) == 0:
            return True

        # If it cannot return right away, check if s is a subsequence
        for char in s:
            if char == s[i]:
                i += 1
                if i == len(s):
                    return True
        
        # If it makes it through without finding s as a subsequence, return false
        return False
        
