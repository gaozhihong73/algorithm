from typing import Counter, List


class Solution:
    """
    三元组，采用枚举中间的方式
    使用两个哈希表，一个保存当前数前边符合条件的数据，一个保存当前元素后边符合条件的数据
    遍历数组，累加所有符合条件的数据
    """

    def specialTriplets(self, nums: List[int]) -> int:
        suf = Counter(nums)
        pre = Counter()

        ans = 0

        for num in nums:
            suf[num] -= 1
            ans += suf[num * 2] * pre[num * 2]
            pre[num] += 1

        return ans % (10**9 + 7)
