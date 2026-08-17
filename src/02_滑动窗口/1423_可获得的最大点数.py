from typing import List


class Solution1:
    """
    逆向思维
    """

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 将题目转化为求长度为 n-1 的，和最小的子子数组，就转化为了普通的滑动窗口题目
        n = len(cardPoints)
        cardPoints_sum = sum(cardPoints)

        if n == k:
            return cardPoints_sum

        target_len = n - k

        left = 0
        min_sum = cardPoints_sum
        cur_sum = 0

        for right in range(n):
            cur_sum += cardPoints[right]

            if right - left + 1 < target_len:
                continue

            min_sum = min(min_sum, cur_sum)

            cur_sum -= cardPoints[left]
            left += 1

        return cardPoints_sum - min_sum


class Solution:
    """
    正向思维
    答案必定是以下子数组的和之一：
        前 k 个数的和。
        前 k−1 个数以及后 1 个数的和。
        前 k−2 个数以及后 2 个数的和。
        ……
        前 2 个数以及后 k−2 个数的和。
        前 1 个数以及后 k−1 个数的和。
        后 k 个数的和。
    直接利用滑动窗口遍历这些结果，取最大值即可
    """

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = s = sum(cardPoints[:k])

        for i in range(1, k + 1):
            s += cardPoints[-i] - cardPoints[k - i]
            ans = max(ans, s)
