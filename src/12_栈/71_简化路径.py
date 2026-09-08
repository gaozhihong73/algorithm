class Solution1:
    """
    模拟
    垃圾写法
    """

    def simplifyPath(self, path: str) -> str:
        dot = 0
        x = 0
        stack = list()
        for i, c in enumerate(path):
            stack.append(c)
            if "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9":
                dot = 0
                x = 0
            elif c == "/":
                x += 1
                if dot == 2 and i - 3 >= 0 and path[i - 3] == "/":
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    while len(stack) > 0 and stack.pop() != "/":
                        pass
                    stack.append("/")
                elif dot == 1 and i - 2 >= 0 and path[i - 2] == "/":
                    stack.pop()
                    stack.pop()
                elif x > 1:
                    while x > 1:
                        stack.pop()
                        x -= 1
                x = 1
                dot = 0
            elif c == ".":
                dot += 1
                x = 0

        if dot == 1 and stack[len(stack) - 2] == "/":
            stack.pop()
            stack.pop()
        elif dot == 2 and stack[len(stack) - 3] == "/":
            stack.pop()
            stack.pop()
            stack.pop()
            while len(stack) > 0 and stack.pop() != "/":
                pass
        n = len(stack) - 1
        if n <= 0:
            return "/"

        while n > 0 and stack[n] == "/":
            stack.pop()
            n -= 1

        return "".join(stack)


class Solution:
    """
    使用库函数 spilt 通过 "/" 字符对原字符串分割
    极大降低题目的难度
    """

    def simplifyPath(self, path: str) -> str:
        stack = []
        sp = path.split("/")
        for s in sp:
            if s == "" or s == ".":
                continue
            elif s != "..":
                stack.append(s)
            elif stack:
                stack.pop()
        return "/" + "/".join(stack)


if __name__ == "__main__":
    print(Solution().simplifyPath(path="/...///a/../b/c/../d/./"))
