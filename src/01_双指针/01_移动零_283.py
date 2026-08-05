from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dest = -1
        for cur in range(len(nums)):
            if nums[cur] != 0:
                dest += 1
                if dest < cur:
                    nums[dest], nums[cur] = nums[cur], nums[dest]
