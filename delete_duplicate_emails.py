"""
LeetCode #196: Delete Duplicate Emails
URL: https://leetcode.com/problems/delete-duplicate-emails/
Difficulty: Easy

Problem:
Write a solution to delete all duplicate emails, keeping only one unique email with the smallest `id`.
For Pandas, modify `person` in-place.

Complexity:
- Time Complexity: O(N log N) — Sorting DataFrame `person` by `id` where N is the number of rows.
- Space Complexity: O(1) — In-place modification of DataFrame `person`.
"""

import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """
    person - Person pandas DataFrame with columns ['id', 'email'] [pd.DataFrame]
    """
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(subset=["email"], inplace=True, keep="first")