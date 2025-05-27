from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = defaultdict(int)
        for item in nums:
            hashset[item] += 1
        for key in hashset:
            if hashset[key] > 1:
                return True
        return False
