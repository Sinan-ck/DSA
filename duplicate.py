"""
Problem: Find Duplicate Numbers
Given a list of integers, find all numbers that appear more than once.

Example:
Input: [1, 2, 2, 3, 3, 3, 4]
Output: {2, 3}

Approach:
- Use a set to track seen numbers (O(1) lookup)
- When we see a number again, add it to duplicates set
- Time: O(n), Space: O(n)
"""

num = list(map(int, input().split()))

seen = set()
duplicates = set()

for i in num:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(duplicates)
