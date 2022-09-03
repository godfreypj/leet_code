class Solution(object):
    

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary
        numeral_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
        result = 0

        for index in range(len(s)-1, -1, -1):
            
            num = numeral_dict[s[index]]

            if 3*num < result:
                result = result-num
            else:
                result = result+num
            
        return result
            
        # Apply the rules of Roman Numerals
        
        # Return