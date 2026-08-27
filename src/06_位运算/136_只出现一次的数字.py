from typing import List


class Solution:
    """
    异或的运算法则：
        a ^ 0 = a
        a ^ a = 0
        a ^ b ^ c = a ^ (c ^ b)
    我们只需要拿 一个 0 去异或 nums 中的每一个数，这样就可以保证相同的两个数相互抵消
    """

    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num

        return ans
