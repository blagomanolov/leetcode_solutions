"""
LeetCode #27: Remove Element
URL: https://leetcode.com/problems/remove-element/
Difficulty: Easy

Problem:
Given an integer array `nums` and an integer `val`, remove all occurrences of `val`
in `nums` in-place. Return the number of elements in `nums` which are not equal to `val`.

Complexity:
- Time Complexity: O(N) — Two-pointer approach traversing array `nums` of length N once.
- Space Complexity: O(1) — In-place modification using constant extra space.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        i - slow_pointer / index for non-val elements [Int]
        j - fast_pointer / current element index [Int]
        val - target value to remove [Int]
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i