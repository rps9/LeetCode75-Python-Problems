class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Define needed variables 
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        collected_vowels = []
        reversed_vowels = ''

        # Collect all of the vowels
        for letter in s:
            if letter in vowels:
                collected_vowels.append(letter)

        # Create variable for iterating in reverse
        i = len(collected_vowels) - 1

        # Place vowels back in reverse order
        for letter in s: 
            if letter in vowels:
                reversed_vowels += collected_vowels[i]
                i -= 1
            else:
                reversed_vowels += letter

        # Return the completed string
        return reversed_vowels
