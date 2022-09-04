"""
This module takes a list of roman numerals and returns
the equivalent decimal
"""
from typing import List

class Solution():
    """Solution class

    Attributes:
        roman_numerals (List[str]): List of roman numerals to convert
        solution (List[str]): List of decimals as per input
    """
    def __init__(self, roman_numerals: List[str]):
        self.roman_numerals = input
        self.solution = []

        for numeral in roman_numerals:
            self.solution.append(self.roman_to_int(numeral))

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Solution):
            return self.roman_numerals is other.roman_numerals and self.solution is other.solution
        return False

    def roman_to_int(self, numeral: str) -> int:
        """ Given a roman numeral string, this function will
        return the equivalent decimal string

        Args:
            numeral (str): the roman numeral to be converted
        Returns:
            result (int): the equivalent decimal
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

        # Zero out the result
        result = 0

        # Iterate backwards over our string numeral
        for index in range(len(numeral)-1, -1, -1):

            # Set num to index
            num = numeral_dict[numeral[index]]

            # Determine if the numeral is before or after
            if 3*num < result:
                # Subtract the numeral from the result
                result = result-num
            else:
                # Add the numeral to the result
                result = result+num

        # Return
        return result

if __name__ == "__main__":
    input_list = ["I", "III", "V", "VII"]
    test = Solution(input_list)
    print(str(test.solution))
