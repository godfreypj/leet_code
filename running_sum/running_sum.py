"""
Module info
"""
from random import randrange
from typing import List

class Solution():
    """
    Solution class instantiates needed items and solution to the
    running sum problem.
    """
    def __init__(self):
        self.nums_to_sum: List[int]     = []
        self.solution: List[int]        = []

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Solution):
            return self.solution is other.solution
        return False

    def running_sum(self):
        """
        Iterates over given list of integers, creating a new
        list that is the sum of each of the elements in the
        original list
        """

        # While building the result array
        while len(self.nums_to_sum) > 0:
            running_sum = 0
            # Iterate over given list, backwards
            for item in reversed(self.nums_to_sum):
                # Sum all elements that came before
                running_sum += item
            # Insert them into the correct position of the result
            self.solution.insert(0, running_sum)
            # Pop off the element we just summed and do it again
            self.nums_to_sum.pop()

if __name__ == "__main__":
    result = Solution()
    result.nums_to_sum = [1,2,3,4,5]
    result.running_sum()
    print(result.solution)
    # Random tests with the following contraints:
    # 1 <= nums.length <= 1000
    # 0 <= nums[i] <= 10^6
    sol_obj = Solution()
    for index in range(1000):
        sol_obj.nums_to_sum.append(randrange(0, 10e6))
    sol_obj.running_sum()
