class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # Find which string is bigger or if they are the same length

        if len(str1) < len(str2):
            smaller_string = str1
            bigger_string = str2
        elif len(str1) > len(str2):
            smaller_string = str2
            bigger_string = str1
        else:
            if str1 == str2:
                return str1
            else: 
                return ''
        
        # Check for largest possible divisers then work your way down until you find a valid one

        i = len(smaller_string)

        while i > 0:
            if (len(smaller_string) % i == 0 and len(bigger_string) % i == 0 and smaller_string[0:i] == bigger_string[0:i] and smaller_string == smaller_string[0:i]*(len(smaller_string) / i) and bigger_string == bigger_string[0:i]*(len(bigger_string) / i)):
                return smaller_string[0:i]
            else: 
                i -= 1

        return ''
