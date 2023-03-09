class Solution:
    def numIdenticalPairs(self, nums) :
        count=0
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                if i<j and nums[i]==nums[j]:
                  count+=1
        return count     
                
p=Solution()
print(p.numIdenticalPairs( [1,2,3,1,1,3]))
