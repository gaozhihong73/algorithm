from typing import List


class Solution:
    """
    结果可由两部分组成：
        1. 老板不生气的总客人数 s0
        2. customers数组中，长度为 minutes 的最大和子数组中的生气部分的客人数 s1
        ans = s0 + s1
    其中：
        1. 直接算即可
        2. 可利用滑动窗口求出
    """

    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # s[0] 表示不生气时候的客人数总和，s[1] 表示长度为 minutes 的子数组中 老板生气时的最大客人数
        s = [0, 0]
        max_s1 = 0
        left = 0
        for right, (c, g) in enumerate(zip(customers, grumpy, strict=False)):
            s[g] += c
            if right - left + 1 < minutes:
                continue

            max_s1 = max(max_s1, s[1])

            if grumpy[left] == 1:
                s[1] -= customers[left]
            left += 1

        return s[0] + max_s1
