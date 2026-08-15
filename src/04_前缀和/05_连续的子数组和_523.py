from collections import defaultdict
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if n < 2:
            return False

        mod_index = defaultdict(int)
        prefix = 0  # 前缀和

        mod_index[0] = -1

        for i in range(n):
            # 同余定理：如果 y mod p == x， 那么 z % p == x ←→ (y - z) % p == 0
            #
            # 反过来就是：如果两个对同一个数取模余数相等，那么这两个数之差（前缀和之差也就是区间之和）对这个数取模结果为0

            prefix += nums[i]
            mod = prefix % k

            if mod in mod_index:
                if i - mod_index[mod] > 1:
                    return True
            else:
                mod_index[mod] = i
        return False
