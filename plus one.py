class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_arr = list(map(str,digits))
        num = int(''.join(str_arr))
        num+=1
        return(list(map(int,list(str(num)))))




# Plus One

This project contains a Python solution for the LeetCode "Plus One" problem.

## Problem
Given a non-empty array of decimal digits representing a non-negative integer, increment the integer by one and return the resulting array of digits.

## Approach
1. Convert the list of digits to a string.
2. Convert the string to an integer.
3. Add one to the integer.
4. Convert the result back to a list of digits.

## Example
Input: [1, 2, 3]
Output: [1, 2, 4]

Input: [9, 9, 9]
Output: [1, 0, 0, 0]

## Language
- Python
