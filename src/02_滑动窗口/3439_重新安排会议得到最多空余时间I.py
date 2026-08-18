from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        """
        本质：是求长度为 n+1 的数组中，长度为 k+1 且总和最大的子数组的和
        解释：
            要开 n 场会，每一场会与下一场会之间都会有空闲时间(可能为0), 那 n 场会之间就会有 n-1 个空闲时间
            加上第一场会之前的空闲时间 和 最后一场会之后的空闲时间 就剩 n+1 个空闲时间
            先跑一轮循环计算出 这n+1个空闲时间 free

            我们要重新安排 k 个会议得到最大的 空闲时间， 安排两个会议就会得到两个会议中间的一段空闲时间，同理 安排 k 个会议 就能得到 k-1 段空闲时间
            再加上 开头和结尾的空闲时间就剩 k+1 段空闲时间，就是要在 free 中找到 和最大的长度为 k+1 的子数组
        """
        n = len(startTime)
        free = [0] * (n + 1)
        # 开头的空闲时间
        free[0] = startTime[0]

        # 每个会议中间的空闲时间
        for i in range(1, n):
            free[i] = startTime[i] - endTime[i - 1]

        # 结尾的空闲时间
        free[n] = eventTime - endTime[n - 1]

        max_free = 0
        cur_free = 0
        left = 0
        for right in range(n + 1):
            cur_free += free[right]

            if right - left + 1 < k + 1:
                continue

            max_free = max(max_free, cur_free)

            cur_free -= free[left]
            left += 1
        return max_free


if __name__ == "__main__":
    Solution().maxFreeTime(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10])
