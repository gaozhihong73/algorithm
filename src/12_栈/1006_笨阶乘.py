class Solution:
    """
    规律：
        每4个数一组，四个数会产生2个结果入栈，最后再对栈中的数进行一加一减操作计算出最终的结果
        举例：
            n = 7 时，需要计算：7 * 6 / 5 + 4 - 3 * 2 / 1
            因为先乘除后加减的计算顺序，可以看作 (7 * 6 / 5) + 4 - (3 * 2 / 1)
            前四个数就可以看作 (7 * 6 / 5) = 8 和 4 两个数，依次类推，(7 * 6 / 5) + 4 - (3 * 2 / 1)就变为了 8 + 4 - 6
            最后转化的结果一加一减计算得到最后的数就是答案

    """

    def clumsy(self, n: int) -> int:
        stack = []
        # 倒序列表
        nums = [i for i in range(n, 0, -1)]
        # 每四个一组，每组入栈2个数
        for i in range(3, n, 4):
            stack.append(nums[i - 3] * nums[i - 2] // nums[i - 1])
            stack.append(nums[i])

        # 最后剩下的不够一组，则额外判断一下
        mod = n % 4
        if mod == 3:
            stack.append(int(nums[n - 3] * nums[n - 2] // nums[n - 1]))
        elif mod == 2:
            stack.append(nums[n - 2] * nums[n - 1])
        elif mod == 1:
            stack.append(nums[n - 1])

        # 采用一加一减计算
        ans = stack[0]

        for i in range(1, len(stack)):
            if i % 2 == 1:
                ans += stack[i]
            else:
                ans -= stack[i]

        return ans


if __name__ == "__main__":
    Solution().clumsy(10)
