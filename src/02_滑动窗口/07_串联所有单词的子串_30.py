from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len = len(s)
        word_len = len(words[0])
        words_len = len(words)
        all_word_len = word_len * words_len

        if s_len < all_word_len:
            return []

        # 统计每个字符串出现了多少次
        hash2 = Counter(words)
        ans = []

        for i in range(word_len):
            hash1 = Counter()
            count = 0
            left = i
            for right in range(
                i, s_len - word_len + 1, word_len
            ):  # s_len - word_len + 1 是为了保证right能访问的到最后一个子串
                in_str = s[right : right + word_len]  # 提取如窗口的子串
                hash1[in_str] += 1  # 统计个数
                if hash1[in_str] <= hash2[in_str]:  # 判断当前子串的有效性
                    count += 1
                if (
                    right - left >= all_word_len
                ):  # 当前遍历的字符串长度 等于 子串的总长度
                    out_str = s[left : left + word_len]  # 提取出窗口的子串
                    if hash1[out_str] <= hash2[out_str]:  # 检查有效性
                        count -= 1
                    hash1[out_str] -= 1
                    left += word_len
                if count == words_len:  # 更新答案
                    ans.append(left)
        return ans


if __name__ == "__main__":
    ans = Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])
    print(ans)
