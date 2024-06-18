class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        # Define variables 
        next_character = ''
        count = 0
        index = 0

        # Iterate through the characters 
        for i in range(0, len(chars)):
            if i == len(chars) - 1:
                # Last character add it to the array
                count += 1
                if count == 1: # If it is the only one then no need to add the number '1'
                    chars[index] = chars[i]
                    index += 1
                else: # If it is not the only one of it's kind then include the number after
                    chars[index] = chars[i] 
                    index += 1
                    for digit in str(count):
                        chars[index] = digit
                        index += 1 # Increase the index by one for every digit and character you add  
            else:
                # Not last character, check stuff
                count += 1 #Add this character to the count of these characters
                next_character = chars[i + 1]
                if chars[i] != next_character: # If the current character is the last one of it's kind, add it 
                    if count == 1: # If it is the only one then no need to add the number '1'
                        chars[index] = chars[i]
                        index += 1
                    else: # If it is not the only one of it's kind then include the number after
                        chars[index] = chars[i]
                        index += 1
                        for digit in str(count):
                            chars[index] = digit
                            index += 1 # Increase the index by one for every digit and character you add
                    count = 0                        
        return index
