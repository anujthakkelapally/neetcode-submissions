class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], index]
            num_index_map[num] = index
        return []
