from typing import List


class Solution:
    """
    先用 xor=0 去 异或 nums 中的所有的数，运算完成后 xor 里面存储的就是那两个只出现一次的数的异或结果
    根据异或的性质 相同为0 相异为1，我们找到 xor 最右侧的 1, 也就是那两个只出现一次的数比特位第一次不同的位置
    可以根据这个结论把 nums 中的数分为两组，两个只出现一次的数肯定分别在不同的组中
    然后再用两个初始值为0的变量分别对这两组进行异或，这两个变量最后的结果就是那两个不同的值
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num

        lsd = xor & (-xor)

        ans = [0, 0]
        for num in nums:
            if num & lsd == 0:
                ans[0] ^= num
            else:
                ans[1] ^= num

        return ans
