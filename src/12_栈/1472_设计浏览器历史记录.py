class BrowserHistory:
    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.index += 1
        # 删除前进的记录，也就是把从当前位置开始到结尾的所有元素删除，然后再插入新的 url
        del self.pages[self.index :]

        self.pages.append(url)

    def back(self, steps: int) -> str:
        if steps > self.index:
            self.index = 0
        else:
            self.index -= steps
        return self.pages[self.index]

    def forward(self, steps: int) -> str:
        if self.index + steps > len(self.pages) - 1:
            self.index = len(self.pages) - 1
        else:
            self.index += steps
        return self.pages[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
