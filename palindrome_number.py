"""
LeetCode #9: Palindrome Number
URL: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy

Problem:
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

Complexity:
- Time Complexity: O(log10(x)) — Reversing the integer digit by digit (number of digits in `x`).
- Space Complexity: O(1) — Constant extra space used for variables `t`, `r`, and `d`.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        t - temp / original number copy [Int]
        r - reversed_number [Int]
        d - last_digit [Int]
        """
        t = x
        r = 0
        if x < 0:
            return False

        while t > 0:
            d = t % 10
            r = r * 10 + d
            t = t // 10

        return r == x