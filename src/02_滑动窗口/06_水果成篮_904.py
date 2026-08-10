from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        left = 0
        hh = defaultdict(int)

        for right, fruit in enumerate(fruits):
            hh[fruit] += 1
            if len(hh) > 2:
                hh[fruits[left]] -= 1
                if hh[fruits[left]] == 0:
                    del hh[fruits[left]]  # 频次归零，删除该水果类型
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
