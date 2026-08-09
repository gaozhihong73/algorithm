from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        # 1. 排序
        nums.sort()
        ans = []

        # 2. 第一层循环：固定第一个数 nums[i]
        # 注意 range 上限是 n - 3，确保后面至少留出 3 个位置
        for i in range(n - 3):
            # 对第一个数去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 第一层剪枝（可选）：如果连续最小的四个数相加都大于 target，后面不可能有解
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 第一层剪枝（可选）：如果 nums[i] 加上最大的三个数都小于 target，当前 nums[i] 太小，跳过
            if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
                continue

            # 3. 第二层循环：固定第二个数 nums[j]
            # 注意 range 上限是 n - 2，确保后面至少留出 2 个位置
            for j in range(i + 1, n - 2):
                # 对第二个数去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 第二层剪枝（可选）
                if (
                    nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target
                ):  # 最小组合太大，直接跳出内层循环
                    break
                if (
                    nums[i] + nums[j] + nums[-2] + nums[-1] < target
                ):  # 当前组合太小，跳过当前 j
                    continue

                # 4. 双指针夹逼法寻找到后两个数
                left = j + 1
                right = n - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        # 去重：跳过重复的元素
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # 指针真正移动到全新的元素上
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return ans
