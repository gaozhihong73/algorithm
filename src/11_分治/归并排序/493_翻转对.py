from typing import List


class Solution:
    """
    需要单独计算，重要翻转对的数量，而不是在排序的分支里面计算的原有是：
        两者的分支条件的不一致的
            排序的分支条件是 temp[i] > temp[j]
            题意中的分支条件是 temp[i] > 2*temp[j]
        所以不能共用，需要单独使用双指针法去统计结果
    """

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0] * n
        return self.merge_sort(nums, temp, 0, n - 1)

    def merge_sort(
        self, nums: List[int], temp: List[int], left: int, right: int
    ) -> int:
        if left >= right:
            return 0

        mid = (left + right) // 2
        ans = 0

        ans += self.merge_sort(nums, temp, left, mid)
        ans += self.merge_sort(nums, temp, mid + 1, right)

        temp[left : right + 1] = nums[left : right + 1]

        # 2. 单独统计跨区间的翻转对（nums[left..mid] 和 nums[mid+1..right] 均已升序）
        j = mid + 1
        for i in range(left, mid + 1):
            # 当 nums[i] > 2 * nums[j] 时，右指针右移
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            # [mid + 1, j - 1] 区间内的所有元素都满足 nums[i] > 2 * nums[k]
            ans += j - (mid + 1)

        i = k = left
        j = mid + 1
        while i <= mid and j <= right:
            if temp[i] <= temp[j]:
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]
                j += 1
            k += 1

        while i <= mid:
            nums[k] = temp[i]
            i += 1
            k += 1
        while j <= right:
            nums[k] = temp[j]
            j += 1
            k += 1

        return ans
