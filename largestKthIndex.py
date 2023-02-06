class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        buckets = [0 for _ in range(100)]

        for num in nums:
            buckets[len(num) - 1] += 1

        index = 99
        while buckets[index] == 0:
            index -= 1


        for i in range(index, -1, -1):
            bucket = buckets[i]
            if k <= bucket:
                break
            k -= bucket

        return sorted(filter(lambda x: len(x) == i + 1, nums))[-k]
