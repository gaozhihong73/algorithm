from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter()

        left = 0
        max_sum = 0
        win_sum = 0

        for right in range(n):
            # 入窗口
            win_sum += nums[right]
            count[nums[right]] += 1

            if right - left + 1 < k:
                continue

            if len(count) == k:
                max_sum = max(max_sum, win_sum)
            """
            利用字典的长度去判断当前区间是否合法
            因为窗口中的元素的固定的,也就是说字典中能存储的键的数量==k, 如果当前字典的长度 != k, 就说明当前字典中存在重复元素
            不断进出窗口, 更新字典, 当字典的长度 == k 时 说明该窗口合法, 更新答案
            """

            # 出窗口
            win_sum -= nums[left]
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        return max_sum


if __name__ == "__main__":
    Solution().maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3)
