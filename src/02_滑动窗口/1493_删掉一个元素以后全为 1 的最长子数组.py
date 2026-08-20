from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        count = 0  # 当前窗口中 0 的个数
        sum_1 = 0  # 当前窗口的和
        left = 0

        for right in range(n):
            sum_1 += nums[right]
            if nums[right] == 0:
                count += 1

            while count > 1:  # 不符合条件
                if nums[left] == 0:
                    count -= 1
                sum_1 -= nums[left]
                left += 1

            max_len = max(
                max_len, sum_1 if count != 0 else sum_1 - 1
            )  # 此处的 if 处理的是全为 1 的情况，因为就算全为1，也必须去掉一个元素，所以可能要 - 1

        return max_len


if __name__ == "__main__":
    Solution().longestSubarray([1, 1, 1])
