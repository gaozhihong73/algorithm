from collections import Counter
from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        n = len(arrivals)
        count = Counter()
        ans = 0
        left = 0
        for right in range(n):
            """
            count 中记录每种物品出现的次数
            若当前物品在长度为w的窗口内已经出现了 m 次，就说明当前物品一定要被丢弃（可以看作直接从数组中剔除，此处直接将其赋值为一个不存在的数字0）


            """
            if count[arrivals[right]] == m:
                ans += 1  # 更新答案
                arrivals[right] = 0  # 丢弃当前数
            else:
                count[arrivals[right]] += 1

            if right - left + 1 < w:
                continue

            # 来到这里说明窗口已满，出窗口
            # 丢弃的数因为就没入 count， 所以也不用出 count
            if arrivals[left] != 0:
                count[arrivals[left]] -= 1
            left += 1

        return ans
