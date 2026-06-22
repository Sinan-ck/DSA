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



Given an array of strings, group the anagrams together.

Approach:
- Use a defaultdict(list) to group words.
- For each string, sort its characters to create a unique key.
- Anagrams produce the same sorted key, so they are stored in the same list.
- Return all grouped lists.

Example:
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Time Complexity: O(n * k log k)
- n = number of strings
- k = average length of a string
- Sorting each string takes O(k log k)

Space Complexity: O(n * k)
- For storing the grouped anagrams in the dictionary.
