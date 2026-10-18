class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [x * x for x in nums]
        nums.sort()

        n = len(nums)

        positive = nums[n // 2:]
        negative = nums[:n // 2]

        return sum(positive) - sum(negative)