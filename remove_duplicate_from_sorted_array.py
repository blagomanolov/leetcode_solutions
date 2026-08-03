"""
LeetCode #26: Remove Duplicates from Sorted Array
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy

Problem:
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. Return the number of unique elements.

Complexity:
- Time Complexity: O(N) — Two-pointer approach traversing array `nums` of length N once.
- Space Complexity: O(1) — In-place modification using constant extra space.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        i - slow_pointer / index of last unique element [Int]
        j - fast_pointer / current element index [Int]
        """
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

