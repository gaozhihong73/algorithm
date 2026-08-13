from typing import List


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        pre = [1] * (n + 2)
        for i in range(1, n + 1):
            pre[i] = nums[i - 1] * pre[i - 1]

        back = [1] * (n + 2)
        for i in range(n, 0, -1):
            back[i] = nums[i - 1] * back[i + 1]

        ans = []
        for i in range(1, n + 1):
            ans.append(pre[i - 1] * back[i + 1])
        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums

        res = [1] * n

        # 第一步：从左往右，res[i] 存的是 nums[i] 左边所有数的乘积
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # 第二步：从右往左，用一个变量记录右边的乘积，乘到 res[i] 上
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))
