"""
Module info
"""
from typing import List

class Solution(object):
    """
    Class info
    """
    def __init__(self):
        self.solution = None

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Solution):
            return self.solution is other.solution
        return False

    def shuffle(self, nums, num):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

if __name__ == "__main__":
    result = Solution()
    print(result.solution)
