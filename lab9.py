class Container:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        result = self.items[self.index]
        self.index += 1
        return result

def main():
    c1 = Container()
    c1.add_item("alpha")
    c1.add_item("beta")
    c1.add_item("gamma")
    c1.add_item("delta")
    for val in c1:
        print(val, end="\t")

if __name__ == '__main__':
    main()

def sequence_generator():
    n = 1
    count = 0
    while count < 15:
        yield n
        n = n * 10 + 1
        count += 1
    raise StopIteration

def main():
    for val in sequence_generator():
        print(val)

if __name__ == '__main__':
    main()

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def main():
    obj = fib()
    for _ in range(100):
        print(next(obj))

if __name__ == '__main__':
    main()