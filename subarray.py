class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        result=[]
        for i in range(len(l)):
            alist=[]
            # for j in range(l[i],r[i]):
            alist=sorted(nums[l[i]:r[i]+1])
            
            Constant=alist[1]-alist[0]
            for k in range(len(alist)-1):
                if alist[k+1]-alist[k]!=Constant:
                   result.append(False)
                   break
                   
            else:
                result.append(True)
               

        return result
