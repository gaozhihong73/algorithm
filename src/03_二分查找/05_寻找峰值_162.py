from typing import List


class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if right == 0:
            return 0

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] >= nums[mid - 1]:
                left = mid
            else:
                right = mid - 1

        return left


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if right == 0:
            return 0

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


"""
1,2,1,3,5,6,4

1 3 4
5 6 4
5 5 6
6 6 6  
"""
