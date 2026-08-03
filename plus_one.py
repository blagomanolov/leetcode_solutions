"""
LeetCode #66: Plus One
URL: https://leetcode.com/problems/plus-one/
Difficulty: Easy

Problem:
You are given a large integer represented as an integer array `digits`.
Increment the large integer by one and return the resulting array of digits.

Complexity:
- Time Complexity: O(N) — String conversions and mapping over N digits.
- Space Complexity: O(N) — Extra space for string representation and result list.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        n - number [Int]
        """
        n = int("".join(map(str, digits)))
        return [int(i) for i in str(n + 1)]