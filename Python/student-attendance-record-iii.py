from collections import Counter
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = Counter(s)
        return False if counter['A'] > 1 or (counter['L'] > 2 and 'LLL' in s) else True
        
