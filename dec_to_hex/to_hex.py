"""
Blah
"""

import math
from typing import List

class Solution():
    """Solution class

    Attributes:
        roman_numerals  (List[str]): List of roman numerals to convert
        solution        (List[str]): List of decimals as per input
    """
    def __init__(self, decimal_input: List[str]):
        self.decimal_input = decimal_input
        self.solution = None
        self.first = True
        self.hex_dict = {
            10 : "a",
            11 : "b",
            12 : "c",
            13 : "d",
            14 : "e",
            15 : "f",
        }
        self.hex_result = []
        self.bin_result = []

        # Iterate over the input, appending the result to the solution attribute
        for dec in decimal_input:
            if dec > 0:
                self.to_hex(dec)
            elif dec < 0:
                self.twos_comp(dec)
            else:
                self.bin_result.append(dec)
                self.__format_solution__(self.bin_result)

    def __eq__(self, other):
        """Overrides the default implementation""" 
        if isinstance(other, Solution):
            return self.decimal_input is other.decimal_input and self.solution is other.solution
        return False

    def __mod_sixteen__(self, num):
        """ returns the remainder of a given num divided by 16
        Args:
            num (int): number to be divided
        Returns:
            num % 16 (int): remainder of num%16
        """
        return num % 16

    def __div_sixteen__(self, num):
        """ returns the quotient of given num and 16, no decimals
        Args:
            num (int): number to be divided
        Returns:
            num / 16: quotient of num and 16
        """
        return math.trunc(num/16)

    def __mod_two__(self, num):
        """ returns the remainder of a given num divided by 2
        Args:
            num (int): number to be divided
        Returns:
            num % 2 (int): remainder of num%16
        """
        return num % 2

    def __div_two__(self, num):
        """ returns the quotient of given num and 2, no decimals
        Args:
            num (int): number to be divided
        Returns:
            num / 2: quotient of num and 2
        """
        return math.trunc(num/2)

    def __add_one__(self, input_string):

        # Validate
        if not input_string:
            return ''

        # Determine the length
        maxlen = len(input_string)

        # Instantiate
        result  = ''
        carry   = 0

        # Iterate over our 10 digits
        i = maxlen - 1

        first = True

        while i >= 0:

            # Add the given amount to the first (last) digit
            if first:
                temp_string = int(input_string[i]) + 1
                first = False
            # Then add 0's for the rest
            else:
                temp_string = int(input_string[i]) + 0

            # If it's a 1
            if temp_string == 2:
                # Carry the 1 over
                if carry == 0:
                    carry = 1
                    result = "%s%s" % (result, '0')
                else:
                    result = "%s%s" % (result, '1')

            # If it's a 1
            elif temp_string == 1:
                if carry == 1:
                    result = "%s%s" % (result, '0')
                else:
                    result = "%s%s" % (result, '1')

            # If it's a 0
            else:
                if carry == 1:
                    result = "%s%s" % (result, '1')
                    carry = 0
                else:
                    result = "%s%s" % (result, '0')

            # Decrement
            i = i - 1

        # If we have carried our 1 over, calculate
        if carry>0:
            result = "%s%s" % (result, '1')

        # Otherwise, add it as is
        return result[::-1]

    def __format_solution__(self, result):
        """ given a list, returns the hex formatted string
        Args:
            result (List): given list of toHex result
        Returns:
            formatted_result (str): a string representing the hex of given dec
        """
        # Instantiate return string
        formatted_result = ""

        # Iterate over the given List
        for item in result:
            # If our number is less than 10, concat it's string equiv
            if item < 10:
                formatted_result += str(item)
            # If it's more than 10 we know it's def less than 16, so refer to our dict
            else:
                formatted_result += str(self.hex_dict[item])

        self.solution = formatted_result
        return formatted_result

    def to_hex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return str(num)

        if num == 1 and self.first or num == 2 and self.first:
            self.first = False
            return str(num)

        if num >= 1:

            self.first = False

            # Get two results, one remainder & divisor of 16
            mod_res = self.__mod_sixteen__(num)
            div_res = self.__div_sixteen__(num)

            # Insert the remainder to the front of our List
            self.hex_result.insert(0, mod_res)

            # If we haven't reached zero, do it again
            if div_res > 0:
                self.to_hex(div_res)

            # Once the quotient is 0, lets format our result
            return self.__format_solution__(self.hex_result)

    def twos_comp(self, dec):
        """
        :type num: int
        :rtype: str
        """
         # Check -1 case first and return right away
        if dec == -1:
            for item in "ffffffff":
                self.bin_result.append(item)
            self.__format_solution__(self.bin_result)

        else:

            # Get two results, one remainder & divisor of 16
            mod_res = self.__mod_two__(abs(dec))
            div_res = self.__div_two__(abs(dec))

            # Insert the remainder to the front of our list
            self.bin_result.insert(0, mod_res)

            # If we haven't reached zero, start over
            if div_res > 0:

                self.twos_comp(div_res)

        # Pad to 8 hex digits
        while len(self.bin_result) < 32:
            self.bin_result.insert(0, 0)

        # Flip it
        for index in enumerate(self.bin_result):
            if self.bin_result[index] == 0:
                self.bin_result[index] = 1
            else:
                self.bin_result[index] = 0

        # String to build
        bin_str = ""

        # Convert to string
        for item in self.bin_result:
            bin_str += str(item)

        # Add one to the binary result
        self.bin_result = self.__add_one__(bin_str)

        # Convert the binary to a base 10 integer
        new_int = int(self.bin_result, 2)

        # Use our handy function to get the Hex
        self.bin_result = self.to_hex(new_int)

        # Return it
        return str(self.bin_result)

if __name__ == "__main__":
    input_list = ["I", "III", "V", "VII", "X", "IL", "L"]