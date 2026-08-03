"""
LeetCode #35: Search Insert Position
URL: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy

Problem:
Given a sorted array of distinct integers `nums` and a `target` value, return the index
if the target is found. If not, return the index where it would be if it were inserted in order.

Complexity:
- Time Complexity: O(log N) — Binary search algorithm on sorted array `nums` of length N.
- Space Complexity: O(1) — Constant extra space.
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        l_i - low_index [Int]
        h_i - high_index [Int]
        m_i - mid_index [Int]
        """
        l_i = 0
        h_i = len(nums) - 1

        while l_i <= h_i:
            m_i = (l_i + h_i) // 2
            if nums[m_i] == target:
                return m_i
            elif nums[m_i] < target:
                l_i = m_i + 1
            else:
                h_i = m_i - 1
        return l_i