# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        left = 0
        right = n - 1

        left_index = -1
        right_index = -1

        # 找左端点
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            left_index = left
        else:
            return [-1, -1]

        # 找右端点
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        right_index = right

        return [left_index, right_index]
