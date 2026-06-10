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

Uses a dictionary to map Roman symbols to integers.
Traverses the string from left to right.
Detects subtractive cases (IV, IX, XL, XC, CD, CM).
Adjusts the total by subtracting twice the previous value and adding the current value.
