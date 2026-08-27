class Solution:
    """
    找规律
    第一行和第最后一行的规律很明显，从第0个和第numRows-1个下标开始以步长为 (numRows - 1) * 2 遍历即可
    难点在中间行，中间行 相邻 两个字符的间隔是不一样的，需要找到这个规律
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    根据如上形状，第2行在原始字符串中的下标为：1, 5, 7, 11, 13， 第三行的下标为：2, 4, 8, 10， step=6
    我们可以得到规律，每一行的第一个数等于行号-1（因为是从0开始的），第二个数等于 step - 行号 + 1，然后这两个数依次 + step 就是后面的坐标，比如 (1, 5) → +6 → (7, 11)
    根据以上规则编码即可，注意下标越界
    """

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        step = (numRows - 1) * 2
        ans = ""

        # 第一行，规律：从下标0开始，每隔 (n-1)*2 个取一个
        for i in range(0, n, step):
            ans += s[i]

        # 中间行
        for row in range(1, numRows - 1):
            i = row
            j = step - row
            while i < n or j < n:
                if i < n:
                    ans += s[i]
                if j < n:
                    ans += s[j]
                i += step
                j += step
        # 最后一行，规律：从下标numRows-1开始，每隔 (n-1)*2 个取一个
        for i in range(numRows - 1, n, step):
            ans += s[i]

        return ans
