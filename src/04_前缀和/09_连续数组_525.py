from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 将所有的 0 全部 变为 -1
        nums = [-1 if x == 0 else x for x in nums]

        n = len(nums)
        prefix = 0

        index = defaultdict(int)  # 存储每个 前缀和值 的 最靠前下标
        index[0] = -1  # 兼容符合条件的区间包含下标为0的元素
        max_len = 0

        for i in range(n):
            prefix += nums[i]
            if prefix in index:
                max_len = max(max_len, i - index[prefix])
            else:
                index[prefix] = i
            """
            如果当前位置(i)的前缀和 在前面某个位置(k)出现过
            那说明 [k+1, i] 这段区间的和为0, 是符合条件的区间, 计算区间长度(i-k), 判断是否是最大值即可
            """

        return max_len
