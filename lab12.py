import random
from abc import ABC, abstractmethod

class Die(ABC):
    def __init__(self, sides, face_up=4):
        self.sides = sides
        self.face_up = face_up

    def __str__(self):
        return f"{type(self).__name__}({self.sides}): {self.face_up}"

    def get_face(self):
        return self.face_up

    @abstractmethod
    def roll(self):
        pass

class Tetrahedron(Die):
    def __init__(self):
        super().__init__(4)

    def roll(self):
        self.face_up = random.randint(1, self.sides)

class Cube(Die):
    def __init__(self):
        super().__init__(6)

    def roll(self):
        self.face_up = random.randint(1, self.sides)

class Octahedron(Die):
    def __init__(self):
        super().__init__(8)

    def roll(self):
        self.face_up = random.randint(1, self.sides)

class Pentagonal_Trapezohedron(Die):
    def __init__(self):
        super().__init__(10)

    def roll(self):
        self.face_up = random.randint(1, self.sides)

class Dodecahedron(Die):
    def __init__(self):
        super().__init__(12)

    def roll(self):
        self.face_up = random.randint(1, self.sides)

class Icosahedron(Die):
    def __init__(self):
        super().__init__(20)

    def roll(self):
        self.face_up = random.randint(1, self.sides)

def main():
    dice = [Tetrahedron(), Cube(), Octahedron(), Pentagonal_Trapezohedron(), Dodecahedron(), Icosahedron()]
    num_rolls = random.randint(1000, 5000)
    same_value_count = 0

    for i in range(num_rolls):
        values = [die.roll() or die.get_face() for die in dice]
        if len(set(values)) == 1:
            same_value_count += 1
            print(f"All dice have the same face value ({values[0]})")

    print("Final face-up values:")
    for die in dice:
        print(die)

if __name__ == '__main__':
    main()
