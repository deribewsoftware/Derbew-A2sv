class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp, presum = [0] * 3, [0] * 4
        presum[0] = 1
        for num in nums:
            dp[num] = (presum[num] + presum[num+1]) % MOD
            presum[num+1] = (presum[num+1] + dp[num]) % MOD
        return presum[-1]
