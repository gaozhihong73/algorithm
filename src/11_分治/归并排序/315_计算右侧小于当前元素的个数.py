from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n  # 记录每个原始位置元素右侧更小数的数量
        index = [i for i in range(n)]  # 记录当前元素对应的原始下标

        # 辅助数组，避免递归时频繁创建新列表
        temp = [0] * n
        index_temp = [0] * n

        self.merge_sort(nums, temp, count, index, index_temp, 0, n - 1)

        # count[i] 已经对应 nums[i] 的结果，直接返回
        return count

    def merge_sort(
        self,
        nums: List[int],
        temp: List[int],
        count: List[int],
        index: List[int],
        index_temp: List[int],
        left: int,
        right: int,
    ):
        # 递归终止条件
        if left >= right:
            return

        mid = (left + right) // 2

        # 递归划分左右子区间
        self.merge_sort(nums, temp, count, index, index_temp, left, mid)
        self.merge_sort(nums, temp, count, index, index_temp, mid + 1, right)

        # 备份当前区间的数值与原始索引
        temp[left : right + 1] = nums[left : right + 1]
        index_temp[left : right + 1] = index[left : right + 1]

        i = left  # 左半部分指针 [left, mid]
        j = mid + 1  # 右半部分指针 [mid + 1, right]
        k = left  # 合并回原数组的指针

        # 降序合并（从大到小）
        while i <= mid and j <= right:
            if temp[i] > temp[j]:
                # temp[i] 大于 temp[j]，因为右侧已按降序排列，
                # 所以 temp[j...right] 共 (right - j + 1) 个数都小于 temp[i]
                count[index_temp[i]] += right - j + 1
                nums[k] = temp[i]
                index[k] = index_temp[i]
                i += 1
            else:
                # temp[i] <= temp[j]，先放入较大的 temp[j]
                nums[k] = temp[j]
                index[k] = index_temp[j]
                j += 1
            k += 1

        # 处理左半边剩余元素
        while i <= mid:
            nums[k] = temp[i]
            index[k] = index_temp[i]
            i += 1
            k += 1

        # 处理右半边剩余元素
        while j <= right:
            nums[k] = temp[j]
            index[k] = index_temp[j]
            j += 1
            k += 1


if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))
