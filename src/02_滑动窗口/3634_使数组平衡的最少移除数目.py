from typing import List


class Solution:
    """
    核心：
        1. 根据题意得出字符的先后顺序是不影响结果的，因为只确定最大最小值即可，并且中间数据的顺序是可以任意删除的，所以我们可以先对数组进行排序。
        2. 排序后，最大最小值不用显示指定，只去比较当前窗口两边的数是否符合条件，窗口两边的符合的话，窗口内的一定符合。
    """

    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        max_len = 0
        left = 0

        for right in range(n):
            while nums[left] * k < nums[right]:
                left += 1
            max_len = max(max_len, right - left + 1)
        return n - max_len


if __name__ == "__main__":
    Solution().minRemoval(nums=[2, 1, 5], k=2)
