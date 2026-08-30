import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_sort(nums, 0, len(nums) - 1, k)

    def quick_sort(self, nums: List[int], left: int, right: int, k: int) -> int:
        """
        使用快速排序思想实现 寻找数组中的第 K 个最大元素
        每轮快速排序把数组分成三个部分 小于pivot的  等于pivot的  大于pivot的
        根据三个部分的数量来判断递归应该走哪个分支，不断缩小寻找的区域
        """
        # 如果该区域只剩下一个元素了，那么这个元素就是第k大的元素
        if left == right:
            return nums[left]

        # 随机选择一个数
        pivot = nums[random.randint(left, right)]

        # 三个指针
        l = left - 1
        i = left
        r = right + 1

        # 一轮快速排序，将当前区域分为三个部分
        while i < r:
            if nums[i] < pivot:
                """
                如果当前元素小于基准值，将其交换到左侧区域
                扩充左侧区域 (++l)，并将当前指针向后移 (i++)
                """
                nums[l + 1], nums[i] = nums[i], nums[l + 1]
                i += 1
                l += 1
            elif nums[i] > pivot:
                """
                如果当前元素大于基准值，将其交换到右侧区域
                扩充右侧区域 (--r)。因为交换过来的新元素还没比较过，所以 i 不移动
                """
                nums[i], nums[r - 1] = nums[r - 1], nums[i]
                r -= 1
            else:
                i += 1
        """
        循环结束后，数组被划分为三个区间：
        [left, l] 是小于 pivot 的元素
        [l + 1, r - 1] 是等于 pivot 的元素
        [r, right] 是大于 pivot 的元素
        """

        # 计算每个部分有多少个元素，这里只需要计算 > pivot 的 和 ==pivot 的数量即可
        b = r - l - 1  # 等于 pivot 的元素的数量
        c = right - r + 1  # 大于 pivot 的元素的数量

        """
        我们要找的是第k大的元素，
            如果 > pivot 的元素的数量 >= k，就说明第 k 大的元素一定在 [r, right] 这个区间内，在这个区间内递归，因为前面区间虽然不一定有序，但是所有数一定小于当前区间内的所有数，所以找第k大的数，可以看作找当前区间内第k大的数，k不用动

            如果 >= pivot 的元素的数量 >= k，就说明第 k 大的元素一定在 [l+1, right] 这个区间内，但是上面的分支已经判断过 > pivot 的情况，所以进入这个分子的话，第k大的元素一定是落到了 等于 pivot 这个区间[l+1, r-1]内，这个区间内的值都是相等的，直接返回

            如果 < pivot 的元素的数量 >= k，就说明第 k 大的元素一定在 [left, l] 这个区间内，在这个区间内递归，因为后面的区间中的数一定都大于当前区间内的数，但是数量不够k个，所以第k大的数落到了当前的左侧区间，当我们缩小范围在当前区间内寻找第k大的元素时已经是把 b + c 个 > 当前区间所有数的数都排除了，在当前区间内找的应该是第 k-b-c 大的数，k需要修改
        """
        if c >= k:
            return self.quick_sort(nums, r, right, k)
        elif b + c >= k:
            return pivot
        else:
            return self.quick_sort(nums, left, l, k - b - c)
