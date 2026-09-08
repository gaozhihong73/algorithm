class Solution:
    """
    题意：
        每删除一个 *，就要删除 * 左边数据的一个字典序最小的字符，同时要保证删除后整个字符串是字典序最小的字符串
        注意：优先保证删除删的是最小的，然后保证删除后剩下的字符串是字典序最小的，例如 aab* 只能删除 a[a]b*，不能删除b，即使删除b后剩下的aa比删除a后剩下的ab更小
        基于上述说明，适合使用贪心算法

        使用26个栈，分别每个小写字母出现的下标，栈顶为最近（最靠右）出现的下标
        当遍历到 * 时，从头开始遍历栈，找字母最小的栈，如果这个字母目前出现多次，找最后出现的那次，弹出栈
    """

    def clearStars(self, s: str) -> str:
        # 为了方便，创建一个副本，将要删除的元素也标记为 *, 最后统一把*过滤掉，这样可以避免最后再通过栈中的下标去排序字符串
        arr = list(s)
        stack = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != "*":
                stack[ord(c) - ord("a")].append(i)
            else:
                for j in range(26):
                    if stack[j]:
                        arr[stack[j].pop()] = "*"
                    break

        return "".join(c for c in arr if c != "*")
