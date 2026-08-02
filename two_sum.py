"""
LeetCode #1: Two Sum
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Problem:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers
such that they add up to `target`. You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Complexity:
- Time Complexity: O(N) — Single pass hash map lookup where N is the length of `nums`.
- Space Complexity: O(N) — Extra memory for storing elements in the `cn` dictionary.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        cn - checked_numbers [Dict]
        i - index [Int]
        e - element_value [Int]
        se - searched_element [Int]
        """
        cn = {}
        for i, e in enumerate(nums):
            se = target - e
            if se in cn:
                return [i, cn[se]]
            cn[e] = i
        return []