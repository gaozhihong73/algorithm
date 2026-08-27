class Solution:
    """
    模拟
    """

    def countAndSay(self, n: int) -> str:
        ans = "1"

        if n == 1:
            return ans

        for _ in range(n - 1):
            cur = ""
            pos = 0
            start = 0

            while pos < len(ans):
                """
                使用两个指针去遍历当前批次的字符串
                遍历完毕后
                    一个指向一个新的字符类型开始的位置
                    一个指向下一个新的字符类型开始的位置
                这个字符类型的数量就是 pos-start，值就是 ans[start]
                统计完毕之后，将start更新到下一个字符串类型开始的位置继续下一轮计算
                """
                while pos < len(ans) and ans[start] == ans[pos]:
                    pos += 1
                cur += str(pos - start)
                cur += str(ans[start])
                start = pos

            ans = cur

        return ans


if __name__ == "__main__":
    Solution().countAndSay(4)
