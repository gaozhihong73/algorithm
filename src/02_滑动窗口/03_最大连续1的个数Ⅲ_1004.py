from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = -1
        left = 0
        for right in range(n):
            if nums[right] == 0:
                k -= 1
                while k < 0:
                    if nums[left] == 0:
                        k += 1
                    left += 1
            max_len = max(max_len, right - left + 1)
        return 0 if max_len == -1 else max_len


if __name__ == "__main__":
    Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
