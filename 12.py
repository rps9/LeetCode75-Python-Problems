# Not scaleable, should be improved

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        num_array = []
        number = num
        while number > 0:
            num_array.append(number % 10)
            number = number // 10  

        answer = ''

        if num > 999:
            # normal
            answer = num_array[3] * 'M'
        if num > 99:
            # handle hundreds
            if num_array[2] == 4:
                # handle 4
                answer += 'CD' 
            elif num_array[2] == 9:
                # handle 9
                answer += 'CM'
            else:
                # normal
                if num_array[2] >= 5:
                    answer += 'D' + 'C' * (num_array[2] - 5)
                else:
                    answer += num_array[2] * 'C'
        if num > 9:
            # handle tens
            if num_array[1] == 4:
                # handle 4
                answer += 'XL' 
            elif num_array[1] == 9:
                # handle 9
                answer += 'XC'
            else:
                # normal
                if num_array[1] >= 5:
                    answer += 'L' + 'X' * (num_array[1] - 5)
                else:
                    answer += num_array[1] * 'X'
        
        # handle ones
        if num_array[0] == 4:
            # handle 4
            answer += 'IV' 
        elif num_array[0] == 9:
            # handle 9
            answer += 'IX'
        else:
            # normal
            if num_array[0] >= 5:
                answer += 'V' + 'I' * (num_array[0] - 5)
            else:
                answer += num_array[0] * 'I'

        return answer
        
        
