class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None for _ in range(len(nums)*2)]
        for index, num in enumerate(nums):
            ans[index], ans[index+len(nums)] = nums[index], nums[index]
        return ans
