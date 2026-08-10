from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] >= target else 0
        min_len = 10**9
        sum = 0
        left = 0
        for right in range(n):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if min_len == 10**9 else min_len
