from collections import Counter


class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s2 < len_s1:
            return False

        count1 = Counter(s1)
        count2 = Counter()

        count = 0  # 标记当前窗口中符合条件的字符种类（不是数量）
        left = 0

        for right in range(len_s2):
            # 若当前字符在 s1 中出现过
            if s2[right] in count1:
                count2[s2[right]] += 1
                # 若当前字符 在当前窗口中出现的次数 == 在s1中出现的次数
                if count2[s2[right]] == count1[s2[right]]:
                    count += 1
            else:
                # 若当前字符没有在 s1 中出现过，说明当前字符 以及当前窗口中的所有字符都不符合规则，直接重制窗口，将窗口移动到当前字符的后一个位置
                left = right + 1
                count2.clear()
                count = 0
                continue

            # 如果窗口长度超过了 s1 的长度，出窗口
            while right - left + 1 > len_s1:
                # 若当前字符在 s1 中出现过
                if s2[left] in count1:
                    # 若当前字符 在当前窗口中出现的次数 == 在s1中出现的次数
                    if count2[s2[left]] == count1[s2[left]]:
                        count -= 1
                    count2[s2[left]] -= 1
                left += 1

            # 若满足条件，直接返回
            if count == len(count1):
                return True

        return False


class Solution:
    """
    更加简洁的写法，直接比较两个哈希表
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s2 < len_s1:
            return False

        count1 = Counter(s1)
        count2 = Counter(s2[:len_s1])

        if count1 == count2:
            return True

        left = 0

        for right in range(len_s1, len_s2):
            # 出窗口
            count2[s2[left]] -= 1
            left += 1
            # 入窗口
            count2[s2[right]] += 1
            # 比较
            if count1 == count2:
                return True

        return False


if __name__ == "__main__":
    Solution().checkInclusion(s1="adc", s2="dcda")
