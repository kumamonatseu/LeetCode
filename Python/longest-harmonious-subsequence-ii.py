from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_list = []
        counter = sorted(Counter(nums).items(), key=lambda a:a[0])
        for i in range(len(counter)-1):
            if counter[i+1][0] == counter[i][0] + 1:
                length_list.append(counter[i][1] + counter[i+1][1])

        return max(length_list) if len(length_list) else 0
