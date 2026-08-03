"""
LeetCode #28: Find the Index of the First Occurrence in a String
URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy

Problem:
Given two strings `needle` and `haystack`, return the index of the first occurrence
of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

Complexity:
- Time Complexity: O(N * M) — Python string .find() method where N is len(haystack) and M is len(needle).
- Space Complexity: O(1) — Constant extra space.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        haystack - text string to search in [Str]
        needle - substring pattern to search for [Str]
        """
        return haystack.find(needle)