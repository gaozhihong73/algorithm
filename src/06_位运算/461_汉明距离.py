class Solution1:
    """
    方法1：依次比较这两个数的最后一个比特位
    """

    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x != 0 or y != 0:
            if (x & 1) != (y & 1):
                ans += 1
            x = x >> 1
            y = y >> 1

        return ans


class Solution:
    """
    方法2：先对这两个数求异或（相同为0，相异为1）, 然后计算 1 的个数
    """

    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
