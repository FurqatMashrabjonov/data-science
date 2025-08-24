class CountingClicker:
    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"count is {self.count}"

    def click(self):
        self.count += 1
        return self

    def reset(self):
        self.count = 0
        return self

    def read(self):
        return self.count


a = CountingClicker()
print(a)
print(a.click().click().read())
