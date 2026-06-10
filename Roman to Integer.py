class Solution:
    def romanToInt(self, s: str) -> int:
        s=list(s)
        dic={'I':1 ,  'V':5 , 'X':10  , 'L':50  , 'C':100 ,'D':500, 'M':1000  }
        x=dic[s[0]]
        for i in range(1,len(s)):
            if  dic[s[i]]>dic[s[i-1]]:
                x-=2*dic[s[i-1]]
                x+=dic[s[i]]
            else:
                x+=dic[s[i]]
        return x               
 

Approach:
- Store Roman numeral values in a hash table.
- Traverse the string from left to right.
- Handle subtractive notation (IV, IX, XL, XC, CD, CM) by adjusting the previous value when a larger numeral follows a smaller one.
- Accumulate the final integer value during traversal.

Time Complexity: O(n)
- Each character is processed exactly once.

Space Complexity: O(1)
- Uses a fixed-size hash table containing only 7 Roman numeral mappings.he current value.
