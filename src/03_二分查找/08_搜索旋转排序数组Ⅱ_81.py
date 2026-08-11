# https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            # 假设 nums[left] == nums[mid] == nums[right]，那么就无法判断 [left, mid] 和 (mid, right) 哪一段是有序的
            # 此时 改变边界，起到将相同的数字排除出区间的作用，重新采用 33 题中的思路
            if nums[0] == nums[mid] and nums[mid] == nums[-1]:
                left += 1
                right -= 1
            elif nums[0] <= nums[mid]:  # 假设 [0, mid) 这段是有序的
                if nums[0] <= target < nums[mid]:  # targer 落在了 [0, mid) 中
                    right = mid - 1
                else:  # targer 落在了 (mid, end] 中
                    left = mid + 1
            else:  # 假设 (mid, end] 这段是有序的
                if nums[mid] < target <= nums[-1]:  # targer 落在了 (mid, end] 中
                    left = mid + 1
                else:  # targer 落在了 [0, mid) 中
                    right = mid - 1

        return False


if __name__ == "__main__":
    Solution().search([1, 0, 1, 1, 1], 0)
