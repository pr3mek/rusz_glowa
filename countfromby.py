class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1):
        self.incr = i
        self.val = v

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)


h = CountFromBy(100, 10)
print(h.val)
print(h.incr)

