class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=dict(zip(indices,s))
        x=dict(sorted(x.items()))
        result= "".join(x.values())
        return result 
 

Approach:
- Used zip() to pair each index with its corresponding character.
- Converted the pairs into a dictionary for index-to-character mapping.
- Sorted the dictionary by keys (target positions) using sorted().
- Reconstructed the original string by joining the sorted character values with join().

Python concepts practiced:
- zip()
- dict()
- sorted()
- items()
- values()
- string concatenation using join()

Time Complexity: O(n log n) due to sorting.
Space Complexity: O(n) for storing the dictionary and result.         
