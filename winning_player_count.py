class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        dic = {}
        cnt = 0

        for k, v in pick:
            if k not in dic:
                dic[k] = {}
            dic[k][v] = dic[k].get(v, 0) + 1

        for k in dic:
            for v in dic[k]:
                if dic[k][v] > k:
                    cnt += 1
                    break

        return cnt
