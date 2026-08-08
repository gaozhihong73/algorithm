from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        if n < 1:
            return

        dest = -1  # 填充后的位置
        cur = 0  # 当前位置
        while dest < n:
            dest += 1 if arr[cur] else 2
            if dest >= n - 1:  # 若填充到最后一个了
                break
            cur += 1

        if dest == n:  # 如果超出一个，说明最后一个数为 0
            arr[n - 1] = 0
            cur -= 1
            dest -= 2

        # 从后向前
        while cur >= 0:
            if arr[cur] != 0:
                arr[dest] = arr[cur]
                dest -= 1
                cur -= 1
            else:
                arr[dest] = 0
                dest -= 1
                arr[dest] = 0
                dest -= 1
                cur -= 1
