# https://leetcode.cn/problems/search-in-rotated-sorted-array/

from typing import List

"""
核心： 在这个类型的数组中，随便取一个子区间，在子区间中随便取一个下标 k 将这个区间分为两部分， [0, k), (k, end] 这两个区间中一定有一个区间是有序的
判断 target 落在哪个区间中，如果是落在有序的区间中，即可通过
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:  # 假设 [0, mid) 这段是有序的
                if nums[0] <= target < nums[mid]:  # targer 落在了 [0, mid) 中
                    right = mid - 1
                else:  # targer 落在了 (mid, end] 中
                    left = mid + 1
            else:  # 假设 (mid, end] 这段是有序的
                if nums[mid] < target <= nums[-1]:  # targer 落在了 (mid, end] 中
                    left = mid + 1
                else:  # targer 落在了 [0, mid) 中
                    right = mid - 1

        return -1 if left > right else left
