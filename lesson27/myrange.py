class Myrange:
    def __init__(self, num: int, step=1):
        self.num = num
        self.step = step
        self.next = 0

    def __len__(self):
        return self.num

    def __iter__(self):
        rez = []
        n = 0
        while n < self.num:
            rez.append(n)
            n += self.step
        return iter(rez)

    def __next__(self):
        if self.next >= self.num:
            self.next = 0
            raise StopIteration
        rez = self.next
        self.next += self.step
        return rez


if __name__ == "__main__":

    c = Myrange(10)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))

    for i in c:
        print(i, end=' ')

    a = Myrange(20, 2)
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))

    for i in a:
        print(i, end=' ')