class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x=[]
        for val in arr2:
            n=arr1.count(val)
            x.extend([val]*n)
        len1 = len(arr1)-len(x)
        arr1=sorted(arr1)
        org_x=set(x)
        for val in arr1:
            if val not in org_x:
                 x.append(val)
        
        return x
              
          

Implemented Relative Sort Array solution by:
- Counting occurrences of arr2 elements in arr1
- Preserving arr2 order in output
- Sorting remaining elements not in arr2
- Appending sorted leftover values to result
