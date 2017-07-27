#next-greater-element-iv

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(findNums)):
            find_flag = False
            for j in range(nums.index(findNums[i]),len(nums)):
                if(nums[j] > findNums[i]):
                    output.append(nums[j])
                    find_flag = True
                    break
                else:
                    pass
            if find_flag == False:
                output.append(-1)
        return output
