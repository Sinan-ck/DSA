class Solution(object):
    def findErrorNums(self, nums):
        s = set()
        duplicate = 0
        for num in nums:
            if num in s:
                duplicate = num
            s.add(num)
        missing = 0
        for i in range(1, len(nums)+1):
            if i not in s:
                missing = i
                break
        return [duplicate, missing]
