class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        buckets = defaultdict(int)
        for num in nums:
            buckets[num] += 1
        return max(buckets, key=buckets.get)
