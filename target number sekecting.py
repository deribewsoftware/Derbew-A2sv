class Solution:
    def targetIndices(self, N: List[int], T: int) -> List[int]:
        c = i = 0
        for n in N:
            if n < T: i += 1
            elif n == T: c += 1
        return range(i, i+c)
