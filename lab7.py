# Author: Drastansh Nadola
# Assignment / Part: HW7
# Date due: 2023-05-03
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

from abc import ABC, abstractmethod

class Superhero(ABC):
    def __init__(self, given_name, nickname):
        self.given_name = given_name
        self.nickname = nickname

    @abstractmethod
    def list_powers(self):
        pass

    def __str__(self):
        return f"{self.given_name} ({self.nickname})"


class Hulk(Superhero):
    def __init__(self, given_name, nickname):
        super().__init__(given_name, nickname)

    def list_powers(self):
        return ["Superhuman Strength", "Superhuman Durability", "Super Leaping", "Superhuman Stamina",
                "Superhuman Speed"]

    def smash(self):
        print(f"{self.nickname} smash")

    def roar(self):
        print(f"{self.nickname} roar")


class IronMan(Superhero):
    def __init__(self, given_name, nickname, suit_color):
        super().__init__(given_name, nickname)
        self.suit_color = suit_color

    def list_powers(self):
        return ["Highly intelligent"]

    def blast(self):
        print(f"{self.nickname} blasts")

    def fly(self):
        print(f"{self.nickname} flies")

    def __str__(self):
        return f"{self.given_name} ({self.nickname})\ncan fly and has a {self.suit_color} colored-suit"


class CaptainMarvel(Superhero):
    def __init__(self, given_name, nickname, energy):
        super().__init__(given_name, nickname)
        if energy < 0:
            raise ValueError("The energy amount can not be negative.")
        self.energy = energy

    def list_powers(self):
        return ["Superhuman Strength", "Superhuman Durability", "Superhuman Speed", "Superhuman Agility",
                "Regenerative Healing Factor"]

    def absorb_energy(self, amount):
        if amount < 0:
            raise ValueError("The absorbed energy amount can not be negative.")
        self.energy += amount

    def photon_blast(self):
        if self.energy > 0:
            print(f"{self.nickname} discharges a blast of {self.energy} strength")
            self.energy = 0

    def __str__(self):
        return f"{self.given_name} ({self.nickname})\ncan absorb energy (currently has: {self.energy})"

from superhero import Superhero
from hulk import Hulk
from ironman import IronMan
from captainmarvel import CaptainMarvel


def main():

    hero = Superhero("Clark Kent", "Superman")
    print(hero)
    print(hero.list_powers())


    hulk = Hulk("Bruce Banner", "Hulk")
    print(hulk)
    print(hulk.list_powers())
    hulk.smash()
    hulk.roar()


    iron_man = IronMan("Tony Stark", "Iron Man", "red")
    print(iron_man)
    print(iron_man.list_powers())
    iron_man.blast()
    iron_man.fly()


    try:
        captain_marvel = CaptainMarvel("Carol Danvers", "Captain Marvel", -10)
    except ValueError as e:
        print(e)

    captain_marvel = CaptainMarvel("Carol Danvers", "Captain Marvel", 50)
    print(captain_marvel)
    print(captain_marvel.list_powers())
    captain_marvel.absorb_energy(25)
    print(captain_marvel)
    captain_marvel.photon_blast()
    print(captain_marvel)
    captain_marvel.photon_blast()
    print(captain_marvel)
    captain_marvel.absorb_energy(-10)


if __name__ == "__main__":
    main()
