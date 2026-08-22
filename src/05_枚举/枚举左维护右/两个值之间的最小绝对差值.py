from math import inf


class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        hx = [inf] * 3  # 用来存储 1 和 2，最近出现的下标
        min_len = inf  # 1 和 2 距离最近的下标

        for i in range(n):
            if nums[i] == 1 or nums[i] == 2:
                hx[nums[i]] = i  # 更新最近的下标
                # 更新最短的下标，3-nums[i] 的目的是为了 让 1 变成 2 ， 让 2 变成 1
                min_len = min(min_len, abs(hx[3 - nums[i]] - i))
        return min_len if min_len < n else -1
