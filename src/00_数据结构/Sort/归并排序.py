class MergeSort:
    def __init__(self, arr: list[int]):
        self.arr = arr
        self.b = [0] * len(self.arr)

    def merge(self, low: int, mid: int, high: int):

        for i in range(low, high + 1):
            self.b[i] = self.arr[i]

        i = k = low
        j = mid + 1

        while i <= mid and j <= high:
            if self.b[i] <= self.b[j]:
                self.arr[k] = self.b[i]
                i += 1
            else:
                self.arr[k] = self.b[j]
                j += 1

            k += 1

        while i <= mid:
            self.arr[k] = self.b[i]
            i += 1
            k += 1

        while j <= high:
            self.arr[k] = self.b[j]
            j += 1
            k += 1

    def merge_sort(self, low: int, high: int):
        if low < high:
            mid = (high + low) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)


if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    ms = MergeSort(arr)
    ms.merge_sort(0, len(arr) - 1)
    print(arr)  # 输出: [1, 2, 5, 5, 6, 9]
