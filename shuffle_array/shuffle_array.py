"""
Shuffle Array - Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn] this module shall return the array in the form
[x1,y1,x2,y2,...,xn,yn].
"""
import math
from random import randrange
from typing import List

class Solution():
    """
    Class Solution instantiates needed Lists and variables.
    Args:
        None
    Attributes:
        nums (List[int]): list of integers to be shuffled
        result (List[int]): shuffled list of integers

    """
    def __init__(self):
        self.nums:      List[int]   = []
        self.result:    List[int]   = []

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Solution):
            return self.nums is other.nums and self.result is other.result
        return False

    def shuffle(self) -> None:
        """
        Given the array nums consisting of 2n elements in the form
        [x1,x2,...,xn,y1,y2,...,yn] this module shall return the array in the form
        [x1,y1,x2,y2,...,xn,yn].
        Args:
            None
        Returns:
            None
        """
        count = 0
        num = math.trunc(len(self.nums)/2)
        # Build the result List
        while len(self.result) < len(self.nums):
            self.result.append(self.nums[count])
            self.result.append(self.nums[count+num])
            count += 1

if __name__ == "__main__":

    # Testing an easily identifiable result
    sol_obj = Solution()
    sol_obj.nums = [1,2,3,4,4,3,2,1]
    sol_obj.shuffle()
    # Testing randomly created list with constraints:
    # - 1 <= n <= 500
    # - nums.length == 2n
    # - 1 <= nums[i] <= 10^3
    sol_obj = Solution()
    for index in range(4, 500, 2):
        for index in range(index):
            sol_obj.nums.append(randrange(1, 10e3))
        sol_obj.shuffle()
        # Reset
        sol_obj.nums = []
        sol_obj.result = []
