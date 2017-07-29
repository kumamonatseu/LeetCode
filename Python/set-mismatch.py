from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        lost_num = (Counter(list(range(1, len(nums)+1)))-counter).items()[0][0]
        repeat_num = sorted(counter.items(), key=lambda a:a[1], reverse=True)[0][0]
        return [repeat_num, lost_num]
