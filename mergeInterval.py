class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(N)
        # Space: O(N)

        min_val = min([x[0] for x in intervals])
        ref = [0] * ((max([x[1] for x in intervals]) - min_val) + 1)
        ref_set = set()
        for start,end in intervals:
            ref[start-min_val] += 1
            ref[end-min_val] -= 1
            if start == end:
                ref_set.add(start)
        
        res = []
        ctr = ref[0]
        i = 0
        while i < len(ref)-1:
            if ctr != 0:
                temp_interval = []
                temp_interval.append(i+min_val)
                if i+min_val in ref_set:
                        ref_set.remove(i+min_val)
                while i < len(ref)-1 and ctr != 0:
                    i += 1
                    if i+min_val in ref_set:
                        ref_set.remove(i+min_val)
                    ctr += ref[i]
                temp_interval.append(i+min_val)
                res.append(temp_interval)
                
            i += 1
            if i < len(ref):
                ctr += ref[i]
        
        for s in ref_set:
            res.append([s,s])
        
        return res
        
