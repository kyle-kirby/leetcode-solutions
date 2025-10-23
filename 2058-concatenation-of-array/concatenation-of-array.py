class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = nums.copy()
        new_nums += nums
        return new_nums
