class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in nums_count.items():
            buckets[count].append(num)
        
        most_freq_elements = []
        for bucket in reversed(buckets):
            for num in bucket:
                most_freq_elements.append(num)
                if len(most_freq_elements) == k:
                    return most_freq_elements
        
        return most_freq_elements