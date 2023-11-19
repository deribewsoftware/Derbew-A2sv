
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=[]

        for i in range(1,len(nums)):
            j=0
            while j<len(nums)-1:
                if j<i and nums[i]==nums[j]:
                    res.append((j,i))
                j+=1
        return len (res)


        
