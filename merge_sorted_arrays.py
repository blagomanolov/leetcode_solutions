"""
LeetCode #88: Merge Sorted Array
URL: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy

Problem:
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order,
and two integers `m` and `n`. Merge `nums1` and `nums2` into a single array sorted in non-decreasing order in-place inside `nums1`.

Complexity:
- Time Complexity: O((m + n) log(m + n)) — Array slicing and sorting combined elements.
- Space Complexity: O(m + n) — Memory for temporary concatenated list.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        nums1 - first sorted array of size m + n [List[int]]
        m - number of initial valid elements in nums1 [Int]
        nums2 - second sorted array of size n [List[int]]
        n - number of elements in nums2 [Int]
        """
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()