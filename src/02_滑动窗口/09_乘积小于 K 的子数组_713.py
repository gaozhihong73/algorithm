from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        mul = 1
        ans = 0
        for right in range(n):
            mul *= nums[right]
            while left <= right and mul >= k:
                mul //= nums[left]
                left += 1

            ans += right - left + 1  # 将这个区间内的所有可能都计算进去
        return ans
