from typing import List


class Solution:
    """
    利用 异或 的运算规则
    先对使用0 先对nums异或再对[1,n]进行异或，得到的就是缺失的两个数的异或值
    然后找到该值最右侧的1，表示这两个缺失值第一个不同比特位
    根据比特位将 nums 和 [1, n] 分为两组，用两个0分别对这两个组做异或操作
    经过两两抵消后，剩下的两个值就是缺失的两个值
    """

    def missingTwo(self, nums: List[int]) -> List[int]:
        xor = 0
        n = len(nums) + 2

        for num in nums:
            xor ^= num

        for i in range(1, n + 1):
            xor ^= i

        lsd = xor & (-xor)

        ans = [0, 0]

        for num in nums:
            if num & lsd == 0:
                ans[0] ^= num
            else:
                ans[1] ^= num

        for i in range(1, n + 1):
            if i & lsd == 0:
                ans[0] ^= i
            else:
                ans[1] ^= i

        return ans
