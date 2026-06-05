class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, value in enumerate(nums):
            difference = target - value 
            if difference in nums_dict:
                return [nums_dict[difference], index]
            else:
                nums_dict[value] = index