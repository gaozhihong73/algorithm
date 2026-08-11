# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/

from typing import List


# 找 CD 区间中最小的
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        end = right

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[end]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# 找AB区间中最大的
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid

        return nums[0] if left == len(nums) - 1 else nums[left + 1]
