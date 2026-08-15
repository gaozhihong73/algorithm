from collections import Counter
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = Counter([0])
        prefix = 0
        ans = 0
        for elem in nums:
            prefix += elem
            mod = prefix % k
            ans += count[mod]
            count[mod] += 1
        return ans


if __name__ == "__main__":
    ans = Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5)
    print(ans)
