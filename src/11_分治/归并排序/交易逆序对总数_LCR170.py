from typing import List


class Solution:
    def reversePairs(self, record: List[int]) -> int:
        temp = [0] * len(record)
        return self.merge_sort(record, temp, 0, len(record) - 1)

    def merge_sort(
        self, record: List[int], temp: List[int], left: int, right: int
    ) -> int:
        if left >= right:
            return 0

        mid = (left + right) // 2
        ans = 0

        ans += self.merge_sort(record, temp, left, mid)
        ans += self.merge_sort(record, temp, mid + 1, right)

        temp[left : right + 1] = record[left : right + 1]

        i = k = left
        j = mid + 1

        while i <= mid and j <= right:
            if temp[i] <= temp[j]:
                record[k] = temp[i]
                i += 1
            else:
                """
                关键点所在，因为归并排序中左右两块是无序的，但是块内是有序的（递增）
                也就是说左边这个块中当前这个数 > 右边块中的某个数
                那么左边这个块中从当前这个数到块末的所有数都大于右边块中的那个数
                长度为 mid - i + 1，也就是说构成了 mid - i + 1 对逆序
                """
                ans += mid - i + 1
                record[k] = temp[j]
                j += 1
            k += 1

        while i <= mid:
            record[k] = temp[i]
            i += 1
            k += 1
        while j <= right:
            record[k] = temp[j]
            j += 1
            k += 1

        return ans
