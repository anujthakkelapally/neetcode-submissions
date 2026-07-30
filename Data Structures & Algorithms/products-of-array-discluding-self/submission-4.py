class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1 for num in nums], [1 for num in nums]
        for index, num in enumerate(nums):
            if index - 1 >= 0:
                prefix[index] *= prefix[index-1] * nums[index-1]
        
        for index in range(len(nums)-1, -1, -1):
            if index + 1 < len(nums):
                postfix[index] *= postfix[index+1] * nums[index+1]
        
        return [pre * post for pre, post in zip(prefix, postfix)]
