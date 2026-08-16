import math
from typing import List


class Solution1:
    """
    前缀和 + 暴力解法 = 超时
    """

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        max_sum = -math.inf

        index = {-1: 0}

        for i in range(n):
            prefix += nums[i]
            index[i] = prefix
            j = i - k
            while j >= -1:
                if (i - j) % k == 0:
                    max_sum = max(max_sum, index[i] - index[j])
                j -= k

        return int(max_sum)


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0  # 前缀和
        max_sum = -math.inf  # 结果 最大和

        index = [math.inf] * k  # 存储每个取模节点的最小值
        index[k - 1] = 0
        """
        这一步操作的目的是: 把下标为 -1 的位置赋值为 0
        
        目的: 当第一次找到长度为 k 的子数组时, 要计算这个区间的和, 就是当前下标的前缀和 - 下标为 -1 位置的前缀和 = [0, 当前下标] 这个区间内子数组的和, 如果下标为 -1 的位置的前缀和 存储的是无穷大, 那么计算出来的也是无穷大, 无意义, 所以需要将前缀和数组中 -1 位置置0

        那为什么是将 k-1 的位置置0呢?
        当前 index 数组存储的是 i % k 的k个结果中, 每个位置的最小值
        第 k+1 个位置, 也就是 -1, 在 python 中 -1 % k == k - 1, 将 -1 位置置0, 就等价于将 k-1 位置置0
        """

        for i in range(n):
            prefix += nums[i]
            j = i % k
            max_sum = max(max_sum, prefix - index[j])
            index[j] = min(index[j], prefix)

        return int(max_sum)


if __name__ == "__main__":
    # ans = Solution1().maxSubarraySum([-1, -2, -3, -4, -5], 4)
    ans = Solution1().maxSubarraySum([1, 2], 1)
    print(ans)
