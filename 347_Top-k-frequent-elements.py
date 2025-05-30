from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        sorted_list=sorted(freq,key=lambda x:freq[x], reverse=True)
        return sorted_list[:k]

               