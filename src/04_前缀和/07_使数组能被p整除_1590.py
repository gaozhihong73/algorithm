from collections import defaultdict
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        同余定理：如果 prefix mod p == x， 那么 z % p == x ←→ (prefix - z) % p == 0
        移项定理： 如果 (prefix - z) % p == x ←---→ z % p == (prefix - x) % p

        sum(nums) % p  == x
        也就是说当前 数组和 距离被p整除 还多出 x
        所以我们要寻找的目标就是：找到一段子数组（最短），使得该子数组的和 % p == x，将该段子数组删除的话，剩下的子数组一定可以被 p 整除
        问：为什么找的是 数组和 % p == x 的子数组，而不是数组和 == x的子数组
        答：因为 【数组和 == x的子数组】 只是 【数组和 % p == x 的子数组】 的一种特例，我们要长度最小的符合条件的子数组肯定需要在符合条件的所有子数组中寻找, 不能在特例中寻找
        """

        x = sum(nums) % p  # 多出来数

        if x == 0:
            return 0

        prefix = 0  # 前缀和
        # key 各个下标前缀和 % p 的结果， value：当前的下标位置
        index = defaultdict(int)
        index[0] = -1

        ans = len(nums)

        for i in range(len(nums)):
            prefix += nums[i]  # 前缀和
            """
            我们需要寻找的是符合这个条件的子数组：(当前位置的前缀和 prefix - 前面某一个位置的前缀和 z) % p == x
            也就是：(prefix - z) % p == x
            根据前面的移项定理得：(prefix - x) % p == z % p
            
            prefix 和 x 目前都是已知的
            前面所有位置的前缀和 % p 的结果, 以及该位置的下标都存储在了 index 字典中
            我们只需要哪着  (prefix - x) % p 的结果去 index 中检索即可, 若存在, 就说明找到了一个符合条件的子数组
            如此循环 找到所有子数组, 取长度最小的那个字数即可
            """
            if (prefix - x) % p in index:
                ans = min(ans, i - index[(prefix - x) % p])
            index[prefix % p] = i

        return ans if ans < len(nums) else -1
