class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val=arrays[0][0]
        max_val=arrays[0][-1]
        ans=0
        for i in range(1,len(arrays)):
            ans = max(ans,
                      abs(arrays[i][-1] - min_val),
                      abs(max_val - arrays[i][0])      )
            min_val = min(min_val,arrays[i][0])
            max_val = max(max_val,arrays[i][-1])          
        return ans  


Given a list of sorted arrays, find the maximum distance between two integers chosen from different arrays.

Approach:
- Track the minimum value and maximum value seen so far from previous arrays.
- For each new array:
  - Compare its maximum element with the global minimum.
  - Compare its minimum element with the global maximum.
- Update the answer with the largest distance found.
- After processing the current array, update the global minimum and maximum.

This ensures that the two numbers are chosen from different arrays.

Example:
Input: [[1,2,3],[4,5],[1,2,3]]
Output: 4

Explanation:
Choose 1 from the first array and 5 from the second array.
Distance = |5 - 1| = 4

Time Complexity: O(n)
- n = number of arrays
- Each array contributes only its first and last elements.

Space Complexity: O(1)
- Uses only a few variables.
