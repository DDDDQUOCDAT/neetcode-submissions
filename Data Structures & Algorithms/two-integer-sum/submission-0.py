class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in num:
                return [num[complement], index]
            else:
                num[value] = index
        