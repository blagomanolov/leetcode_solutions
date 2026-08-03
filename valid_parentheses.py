"""
LeetCode #20: Valid Parentheses
URL: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Problem:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Complexity:
- Time Complexity: O(N) — Single pass iteration through string `s` of length N.
- Space Complexity: O(N) — Stack `r` stores up to N opening brackets in the worst case.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        s - string [Str]
        r - result_stack [List]
        e - string_element [Str]
        d_p - dictionary_parentheses [Dict]
        l_e - last_element [Str]
        """    
        d_p = {")": "(", "}": "{", "]": "["}
        r = []
        for e in s:
            if e in d_p:
                if len(r) == 0:
                    return False
                l_e = r.pop()
                if d_p[e] != l_e:
                    return False
            else:
                r.append(e)
        return len(r) == 0