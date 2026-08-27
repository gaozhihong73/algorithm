from typing import List


class Solution:
    """
    优化算法：
        计算当前数x的时候， x>>1 的结果一定已经算出来了
        x 比 x>>1 多一个比特位，只需要计算那最后一个比特位是0还是1，然后复用 x>>1 的结果即可
    """

    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(n + 1):
            ans[i] = (ans[i >> 1]) + (i & 1)

        return list(ans)
