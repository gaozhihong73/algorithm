from typing import List


class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        # 判断特殊情况
        if records[0] != 0:
            return 0

        n = len(records)
        if records[-1] != n:
            return n

        left, right = 0, n - 1

        # 寻找正确序列的最后一个位置，下一个位置就是缺失的人的编号
        while left < right:
            mid = left + (right - left + 1) // 2

            # 如果当前人位置正确，left 向后移动，注意是 = ， 因为 left 可能就是最后一个正确的位置
            if mid == records[mid]:
                left = mid
            else:  # 位置不正确，right 就大胆往前移动
                right = mid - 1

        return left + 1
