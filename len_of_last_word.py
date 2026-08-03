"""
LeetCode #58: Length of Last Word
URL: https://leetcode.com/problems/length-of-last-word/
Difficulty: Easy

Problem:
Given a string `s` consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Complexity:
- Time Complexity: O(N) — String strip and split operations traverse string `s` of length N.
- Space Complexity: O(N) — List of split word strings stored in memory.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        s_s - strip_string [Str]
        w - word [Str]
        """
        s_s = s.strip()
        return len([w for w in s_s.split(" ") if w][-1])