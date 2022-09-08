"""
Given a list of integers, this module will return the number of 
pairs in the list.
"""

from random import randrange
from typing import List

class Solution():
    """
    Solution class
    Attributes:
        solution (int): the number of pairs
        nums (List[int]): the list to check for pairs
    """
    def __init__(self):
        self.solution: int = 0
        self.nums: List[int] = []

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Solution):
            return self.solution is other.solution and self.nums is other.nums
        return False

    def good_pairs(self) -> None:
        """
        Good pairs will take the nums list and determine how many
        pairs of integers are in the given list
        Args:
            None
        Returns:
            solution (int): number of good pairs
        """

        temp_count = 0

        # temp_count is used as our index to compare
        while temp_count < len(self.nums):
            # Starting at one greater than our list_index only compare elements that come ater
            for list_index in range(temp_count+1, len(self.nums)):
                # If we've got a good pair, increment our solution
                if self.nums[temp_count] == self.nums[list_index]:
                    self.solution += 1
            # Increment our index to compare
            temp_count += 1

if __name__ == "__main__":
    # Straight forward solution
    result = Solution()
    result.nums = [1,2,3,1,1,3]
    result.good_pairs()
    print(result.solution)
    # Random tests with the following contraints:
    # Probably a better way than random to create a list with pairs though
    # 1 <= nums.length <= 100
    # 1 <= nums[i] <= 100
    sol_obj = Solution()
    for index in range(100):
        for index in range(index):
            sol_obj.nums.append(randrange(1, 100))
        sol_obj.good_pairs()
        print(sol_obj.solution)
