from typing import List


class Solution1:
    """
    哈希法
    """

    def missingNumber(self, nums: List[int]) -> int:
        lookup = set(nums)
        for i in range(len(nums) + 1):
            if i not in lookup:
                return i
        return 0


class Solution:
    """
    位运算法
    根据异或的运算规则，先用0把nums里面的数都异或一遍
    然后再用这个结果把 [0, n] 都异或一遍，两两抵消，剩下的那个数就是结果
    """

    def missingNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num

        for i in range(len(nums) + 1):
            ans ^= i
        return ans
