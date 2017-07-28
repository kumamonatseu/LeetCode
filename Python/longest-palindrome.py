# Time:  O(n)
# Space: O(1)

# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        for k, v in collections.Counter(s).iteritems():
            odds += v & 1
        return len(s) - odds + int(odds > 0)

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = sum(map(lambda x: x & 1, collections.Counter(s).values()))
        return len(s) - odd + int(odd > 0)

###    
    from collections import Counter
    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == []:
            return 0
        judgement_count = 0
        odd = 0
        a = sorted(Counter(s).items(), key=lambda a:a[1], reverse=True)
        for i in xrange(len(a)):
            if a[i][1] %2 == 0:
                judgement_count += a[i][1]
            else:
                judgement_count += a[i][1] - 1
                odd = 1
        return judgement_count + odd
