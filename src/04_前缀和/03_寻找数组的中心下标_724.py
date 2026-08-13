from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = nums[i - 1] + prefix[i - 1]

        for i in range(1, n + 1):
            if prefix[i - 1] == prefix[n] - prefix[i]:
                return i - 1

        return -1
