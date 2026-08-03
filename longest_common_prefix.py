"""
LeetCode #14: Longest Common Prefix
URL: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy

Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

Complexity:
- Time Complexity: O(S) — where S is the sum of all characters in all strings.
- Space Complexity: O(1) — Memory for intermediate prefix string.
"""

from typing import List

class Solution:
    def _take_substring(self, e: str, t: str):
        """
        e - element [Str]
        t - target [Str]
        r - result [Str]
        """
        r = ""
        for i in range(min(len(e), len(t))):
            if e[i] == t[i]:
                r += e[i]
            else:
                break
        return r

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        l_s - length_list [Int]
        f_e - first_element [Str]
        ss - searched_substring [Str]
        n_ss = new_substring [Str]
        """
        l_s = len(strs)
        if l_s == 0:
            return ""
        elif l_s == 1:
            return strs[0]
        else:
            f_e = strs[0]
            ss = f_e
            for e in strs[1:]:
                n_ss = self._take_substring(e, ss)
                if len(ss) < len(n_ss):
                    continue
                ss = n_ss
            return ss
                