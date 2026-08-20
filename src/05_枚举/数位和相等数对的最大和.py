from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        lookup = defaultdict(int)  # 键：数位和    值：得出该数位和的最大的数
        max_sum = 0

        for i in range(n):
            s = self.sum_i(nums[i])  # 计算数位和
            if s in lookup:
                max_sum = max(max_sum, nums[i] + lookup[s])  # 更新最大值
                if nums[i] > lookup[s]:  # 更新数位和
                    lookup[s] = nums[i]
            else:
                lookup[s] = nums[i]

        return -1 if max_sum == 0 else max_sum

    def sum_i(self, num: int) -> int:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10

        return s


if __name__ == "__main__":
    Solution().maximumSum([18, 43, 36, 13, 7])
