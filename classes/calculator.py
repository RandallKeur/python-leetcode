"""Class to represent a calculator"""
from typing import List


class Calculator:
    """Class to represent a calculator"""

    def max_width_ramp(self, nums: List[int]) -> int:
        """Calculate the maximum width ramp value of a list"""
        stack_of_indices = self.build_stack_of_desc_values_indices(nums)
        return self.find_max_width_ramp(nums, stack_of_indices)

    @staticmethod
    def find_max_width_ramp(numbers: List[int], stack_of_indices: []) -> int:
        """Find the maximum width ramp value based list of numbers and stack of indices"""
        size = len(numbers)
        max_width = 0
        for j in range(size - 1, -1, -1):
            while stack_of_indices and numbers[stack_of_indices[-1]] <= numbers[j]:
                max_width = max(max_width, j - stack_of_indices.pop())

        return max_width

    @staticmethod
    def build_stack_of_desc_values_indices(nums: List[int]) -> []:
        """Build the stack of indices for values in decreasing order"""
        size = len(nums)
        stack = []
        for i in range(size):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        return stack