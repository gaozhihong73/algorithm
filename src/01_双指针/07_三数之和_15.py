class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        # 边界条件判断：少于 3 个数直接返回空
        if n < 3:
            return []

        # 1. 排序：方便双指针夹逼与去重
        nums.sort()

        # 如果最小值都大于 0，不可能凑成和为 0
        if nums[0] > 0:
            return []

        ans = []

        # 2. 固定第一个数 nums[i]
        for i in range(n - 2):
            # 剪枝：如果当前固定值大于 0，由于数组已排序，后续相加必然大于 0
            if nums[i] > 0:
                break

            # 对第一个数去重：如果和前一个元素相同，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            # 3. 双指针寻找另外两个数
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    # 跳过左指针方向重复的元素（停在最后一个重复值上）
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过右指针方向重复的元素（停在最后一个重复值上）
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 关键一步：将指针真正移动到下一个未处理的全新元素
                    left += 1
                    right -= 1

                elif s < 0:
                    # 和偏小，左指针右移增大数值
                    left += 1
                else:
                    # 和偏大，右指针左移减小数值
                    right -= 1

        return ans
