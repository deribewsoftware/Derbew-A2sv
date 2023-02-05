import heapq
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(nums):
            return "0"
        class key:
            def __init__(self,num):
                self.num = num
            def __lt__(self,other):
                return self.num+other.num > other.num+self.num
        heap = []
        for i in nums:
            heapq.heappush(heap,key(str(i)))
        res = ""
        while heap:
            res += heapq.heappop(heap).num
        return res
        
