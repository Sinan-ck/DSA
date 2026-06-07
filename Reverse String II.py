class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = 0

        while n < len(s):
            n += k
            print(n)

            if (n // k) % 2 != 0:
                s = s[:n-k] + s[n-k:n][::-1] + s[n:]

        return s

   

Approach:
- Iterated through the string in blocks of size k.
- Used a counter to identify alternating k-length segments.
- Reversed characters in odd-numbered segments using Python string slicing ([::-1]).
- Reconstructed the string by concatenating:
  - the unchanged prefix,
  - the reversed substring,
  - the remaining suffix.
- Leveraged Python's immutable string handling by creating a new string after each modification.

Key Python concepts used:
- while loops
- string slicing
- reverse slicing ([::-1])
- string concatenation
- conditional logic

Time Complexity: O(n)
Space Complexity: O(n)
