class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Define vowels and running count of vowels in window
        current_vowels = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Initialize the window with all of the data in between
        for letter in s[:k]:
            if letter in vowels:
                current_vowels += 1
        max_vowels = current_vowels

        # Only care about the letter entering and leaving the window, so check if those are vowels
        for i in range(len(s) - k):
            if s[i] in vowels:
                current_vowels -= 1
            if s[i+k] in vowels:
                current_vowels += 1
            max_vowels = max(current_vowels, max_vowels)

        return max_vowels
