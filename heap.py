class Solution:
    def kClosest(self, P, k):
        euclidean = lambda p : p[0]**2 + p[1]**2
        def partition(L, R):
            random = randint(L, R)                 # choosing random pivot
            P[R], P[random] = P[random], P[R]      # and swapping it to the end
            i, pivotDist = L, euclidean(P[R])
            for j in range(L, R+1):
                if euclidean(P[j]) <= pivotDist:
                    P[i], P[j] = P[j], P[i]
                    i += 1
            return i-1
        
        L, R, p = 0, len(P)-1, len(P)
        while p != k:
            p = partition(L, R)
            if p < k:   L = p + 1
            else    :   R = p - 1
        return P[:k]
