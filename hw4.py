class Container:
    def __init__(self):
        self.data = []
        self.size = 0

    def __str__(self):
        return str(self.data)

    def add_item(self, item):
        self.data.append(item)
        self.size += 1

    def remove_item(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of bounds.')
        item = self.data.pop(index)
        self.size -= 1
        return item

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of bounds.')
        return self.data[index]

    def __setitem__(self, index, item):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of bounds.')
        item = self.data[index]

    def __contains__(self, item):
        if item in self.data:
            return True
        else:
            return False

    def __add__(self, rhs):
        new_container = Container()
        new_container.data = self.data + rhs.data
        return new_container



def main():
c1 = Container() # creates an empty container c1.add_item("alpha")
c1.add_item("beta")
print("c1 stringified:", c1)
print("c1 length:", len(c1))
print("c1 contents:")
for idx in range(len(c1)):
print("\t", c1[idx])
c1.add_item("gamma")
c1.add_item("delta")
c1[0] = "omicron" # sets first element to "omicron" from "alpha" c1.remove_item(1) # removes beta
print()
print("c1 length:", len(c1))
print("c1 contents:")
for idx in range(len(c1)):
print("\t", c1[idx])
print()
print("c1 contains zeta:", "zeta" in c1) print("c1 contains alpha:", "alpha" in c1)
c2 = Container() c2.add_item("sigma") c2.add_item("nu") c2.add_item("mu")
c3 = c1 + c2
print()
print("c3 length:", len(c3)) print("c3 contents:")
for idx in range(len(c3)):
print("\t", c3[idx])
print() try:
c3.remove_item(-1) except IndexError as ie:
print("Attempting to remove an item:", ie)
try: print(c3[-1])
except IndexError as ie: print("Attempting to get item:", ie)
try:
c3[-1] = "foo"
except IndexError as ie: print("Attempting to set item:", ie)
try:
c4 = int(10)
c5 = c3 + c4
except TypeError as te:
print("Attempting to add a non-Container:", te) if __name__ == "__main__":
main()
