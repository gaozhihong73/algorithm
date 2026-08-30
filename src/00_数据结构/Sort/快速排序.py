import random


class QuickSort:
    """
    快速排序
    """

    def __init__(self, arr: list[int]):
        self.arr = arr

    def partition(self, low: int, high: int):
        pivot = self.arr[low]
        while low < high:
            while low < high and self.arr[high] >= pivot:
                high -= 1
            self.arr[low] = self.arr[high]
            while low < high and self.arr[low] <= pivot:
                low += 1
            self.arr[high] = self.arr[low]
        self.arr[low] = pivot
        return low

    def quick_sort(self, low: int, high: int):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)


class QuickSort_Plus:
    """
    快速排序 改进版
    """

    def __init__(self, arr: list[int]):
        self.arr = arr

    def quick_sort(self, low: int, high: int):
        if low >= high:
            return
        pivot = self.arr[random.randint(low, high)]
        l = low - 1  # l 指向严格小于 pivot 区间的最后一个元素
        r = high + 1  # r 指向严格大于 pivot 区间的第一个元素
        i = low  # i 是当前遍历的指针

        while i < r:
            if self.arr[i] < pivot:
                """
                如果当前元素小于基准值，将其交换到左侧区域
                扩充左侧区域 (++l)，并将当前指针向后移 (i++)
                """
                self.arr[l + 1], self.arr[i] = self.arr[i], self.arr[l + 1]
                i += 1
                l += 1
            elif self.arr[i] > pivot:
                """
                如果当前元素大于基准值，将其交换到右侧区域
                扩充右侧区域 (--r)。因为交换过来的新元素还没比较过，所以 i 不移动
                """
                self.arr[i], self.arr[r - 1] = self.arr[r - 1], self.arr[i]
                r -= 1
            else:
                i += 1

        self.quick_sort(low, l)
        self.quick_sort(r, high)


if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    qs = QuickSort_Plus(arr)
    qs.quick_sort(0, len(arr) - 1)
    print(arr)  # 输出: [1, 2, 5, 5, 6, 9]
