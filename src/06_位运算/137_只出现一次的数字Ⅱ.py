from typing import List


class Solution:
    """
    计算每个数组中每个比特位的和，如果能被3整除，那么说明那个只出现一次的数改位为0
    反之为1，但是在python中主要注意最高位的时候要做特殊处理
    """

    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            s = sum((num >> i) & 1 for num in nums) % 3
            if s == 1:
                if i == 31:
                    """
                        python 最高位要特殊处理
                        因为最高位是1的话表示这是一个复数
                        需要减去 2^31
                        不然的话就会变成一个非常大的正数
                    """
                    ans -= 1 << i
                else:
                    ans |= 1 << i
        return ans
