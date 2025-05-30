class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l1=set()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        l1.add(triplet)


        return [list(t) for t in l1]                