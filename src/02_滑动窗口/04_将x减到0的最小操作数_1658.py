from typing import List


class Solution:
    # 反向思考 找到一个 和为 sum - x 的最长连续子数组，就找到了 和为 x 的最短两端子数组
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        if nums[0] > x and nums[n - 1] > x:
            return -1
        target = sum(nums) - x
        left = 0
        max_len = -1
        s = 0
        for right in range(n):
            s += nums[right]
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                max_len = max(max_len, right - left + 1)
        return -1 if max_len == -1 else n - max_len
