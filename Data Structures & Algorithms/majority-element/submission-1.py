class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = None
        votes = 0
        for num in nums:
            if candidate is None:
                candidate = num
            if candidate != num:
                votes -= 1
            if votes == 0:
                candidate = num
            votes += 1

        return candidate