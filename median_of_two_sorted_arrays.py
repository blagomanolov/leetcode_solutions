"""
LeetCode #4: Median of Two Sorted Arrays
URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
Difficulty: Hard

Problem:
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively,
return the median of the two sorted arrays.

Complexity:
- Time Complexity: O((m + n) log(m + n)) — Merging arrays and sorting.
- Space Complexity: O(m + n) — Memory for storing the merged array `m`.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        m - merged [List]
        l - merged_len [Int]
        """
        m = nums1 + nums2
        m.sort()
        l = len(m)
        if l % 2 == 0:
            return (m[l // 2 - 1] + m[l // 2]) / 2.0
        return float(m[l // 2])