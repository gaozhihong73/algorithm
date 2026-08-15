from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter([0])

        ans = 0
        s = 0

        for i in range(n):
            s += nums[i]
            ans += counter[s - k]
            counter[s] += 1
        return ans


if __name__ == "__main__":
    Solution().subarraySum(nums=[1, 1, 1], k=2)
