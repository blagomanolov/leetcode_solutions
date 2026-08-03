"""
LeetCode #13: Roman to Integer
URL: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy

Problem:
Given a roman numeral string `s`, convert it to an integer.

Complexity:
- Time Complexity: O(N) — Single pass iteration through string `s` of length N.
- Space Complexity: O(1) — Fixed size hash map `r_d` for 7 Roman numeral symbols.
"""
from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        s - sting representation of roman number [Str]
        r_d - roman_digit_mapping [Dict[str, int]] 
        r - result [Int]
        """
        r_d: Dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1_000,
        }
        r: int = 0
        for i in range(len(s)):
            if i+1<len(s):
                if r_d[s[i]] < r_d[s[i+1]]:
                    r -= r_d[s[i]]
                else:
                    r += r_d[s[i]]
            else:
                r += r_d[s[i]]
        return r