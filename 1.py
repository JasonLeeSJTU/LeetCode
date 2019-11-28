class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            res = target - num
            if res not in h:
                h[num] = i
            else:
                return [h[res], i]
