from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        index = 0  # 记录栈中最后一个位置元素的下标
        stack = []
        count = 0  # 记录需要删除的次数
        for num in nums:
            if len(stack) > 0 and index % 2 == 1 and num == stack[-1]:
                """
                因为题目的要求是，对于 i % 2 == 0 的下标 i ，nums[i] != nums[i + 1]
                最终的数组（栈）中第偶数位置的元素不能后后一个位置相等
                也也可以理解为第奇数个元素不能和前一个位置的相等（这样更简单一点）
                然后判断 如果当前入栈的是栈中第奇数个并且还和栈顶元素相等，那么这两个元素必须要删除一个（此处直接不入栈即可，相应的不如栈的话，index也不用更新，只更新删除的次数即可）
                不满足如上条件的直接入栈即可
                """
                count += 1
            else:
                stack.append(num)
                index += 1

        # 最后要求结果数组的长度必须为偶数，判断如果栈的长度为奇数，那必须要删除一个元素，这里删除最后一个元素，不会破坏前面元素的特性。
        if len(stack) % 2 != 0:
            count += 1

        return count


if __name__ == "__main__":
    print(Solution().minDeletion(nums=[1, 1, 2, 2, 3, 3]))
