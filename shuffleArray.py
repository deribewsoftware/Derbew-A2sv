class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:]
        res=[]
        for i in range(len(x)):
             res.append(x[i])
             res.append(y[i])
        return res
        

        
