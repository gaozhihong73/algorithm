import random
from typing import List


class Solution:
    """
    和 215_数组中的第K个最大元素 的思路基本一样
    通过 k 去自动选择要递归的区域，不断缩小区域
    因为不要求 最小k个数的返回次序，所以想到快排，只要确定此次排序是以第k个数为基准的，那么前面的所有数必定小于k，直接返回该区间内的数即可
    """

    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        self.quick_sort(arr, 0, len(arr) - 1, k)
        return arr[0 : k + 1]

    def quick_sort(self, arr: List[int], left: int, right: int, k: int):
        if left >= right:
            return

        pivot = arr[random.randint(left, right)]
        l = left - 1
        r = right + 1
        i = left

        while i < r:
            if arr[i] < pivot:
                arr[l + 1], arr[i] = arr[i], arr[l + 1]
                i += 1
                l += 1
            elif arr[i] > pivot:
                arr[i], arr[r - 1] = arr[r - 1], arr[i]
                r -= 1
            else:
                i += 1
        a = l - left + 1
        b = r - l - 1

        if a > k:
            self.quick_sort(arr, left, l, k)
        elif a + b >= k:
            """
            如果第k个数落在了第二个区间内，因为第二个区间内的元素值都一样，且第一区间内的所有数都小于第二个区间内的元素
            这样就不用管具体落到第二个区间内的那个位置了，前k个一定是数组中最小的k个，直接返回
            """
            return
        else:
            self.quick_sort(arr, r, right, k - a - b)
