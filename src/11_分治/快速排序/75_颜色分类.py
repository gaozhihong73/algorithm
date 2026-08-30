from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low = -1  # 指向0的最后一个位置，初始为 -1
        high = n  # 指向2的第一个位置，初始为 n
        i = 0  # 遍历指针

        while i < high:  # 当 i == high 时，说明排序已完成
            if nums[i] == 0:  # 碰到0时，将low后一个位置的元素和当前元素交换
                nums[low + 1], nums[i] = nums[i], nums[low + 1]
                self.swep(nums, low + 1, i)
                low += 1
                i += 1  # 此时指针向后走，因为一定是将0交换到前面，也就是说这次交换一定不会破坏规则
            elif nums[i] == 2:  # 当遇到 2 时，将 high 前一个位置的与与当前元素交换
                # 换到后面的一定是2，但是换到前面的不一定是什么，也可能是2，如果这种情况 i++ 的话就将换到前面的2跳过了，破坏了规则。
                nums[i], nums[high - 1] = nums[high - 1], nums[i]
                high -= 1
            else:
                i += 1
