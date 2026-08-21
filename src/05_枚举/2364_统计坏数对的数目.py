from typing import Counter, List


class Solution:
    """
    正面思路不好实现，转化思路。
    符合题意的条件为 j-i != nums[j]-nums[i]
    移项后得：j-nums[j] != i-nums[i]
    还是不太好求，因为这个 != 的情况，不好确定具体的个数
    再次转变思路：假设都符合条件的话，根据求和公式会有  n * (n - 1) // 2 个
    那么 j-nums[j] == i-nums[i] 的就是不符合条件的，那直接去求 j-nums[j] == i-nums[i] 的个数，答案就是 total-去这个数
    这样会简单很多
    """

    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        count = 0
        lookup = Counter()

        for i in range(n):
            count += lookup[i - nums[i]]
            lookup[i - nums[i]] += 1

        return total - count
