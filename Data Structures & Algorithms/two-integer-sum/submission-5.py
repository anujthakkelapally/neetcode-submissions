class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            # num + complement = target
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        
        return None 
