from typing import Counter, List


class Solution1:
    """
    当前属于暴力解法的优化版
    使用两个哈希表一个存储二维数据中每一行有多少个1，一个存储二维数组中每一列有多少个1
    然后遍历整个二维数组，当当前位置值为1的话，就试图计算当前位置所构成的直角三角形的个数
    计算方式为 当前和行的1的个数减1 乘以 当前列的1的个数减1   减1是因为当前位置的值也是1
    """

    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        row_hash = Counter()
        col_hash = Counter()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    row_hash[i] += 1
                    col_hash[j] += 1

        ans = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (row_hash[i] - 1) > 0 and (col_hash[j] - 1) > 0:
                    ans += (row_hash[i] - 1) * (col_hash[j] - 1)

        return ans


class Solution:
    """
    优化后的写法：
        先只计算 每一列 1 出现的次数，并且在每一列的基础上减一，计算结果时候可以直接拿来使用
        然后逐行遍历二维数组，先计算出当前行中 1 出现的次数，同理 也需要减一
        然后计算当前行中的所有为1的元素 一共 可以形成多少个直角三角形
        更新 答案
    """

    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        # 计算每一列 1 出现的次数（结果-1）
        col_num = [sum(col) - 1 for col in zip(*grid, strict=False)]
        ans = 0
        for row in range(row_len):
            # 计算当前行 1 出现的初始（结果-1）
            row_num = sum(grid[row]) - 1
            # 如果当前行减去当前数之后没有别的1了，那么该行的所有值都不可能形成直角三角形，直接跳过当前行
            if row_num <= 0:
                continue
            # 计算当前行中的所有为1的元素 一共 可以形成多少个直角三角形（col_num中存储着每一列除了当前自身外 1 出现的次数）
            ans += row_num * sum(
                col_num[col] for col in range(col_len) if grid[row][col] == 1
            )
        return ans


if __name__ == "__main__":
    Solution().numberOfRightTriangles(grid=[[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
