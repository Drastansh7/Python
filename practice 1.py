class Character:
    def __init__(self,Name,Type,Attack,Defense,HealthPoints, StaminaPoints):
        self.name = Name
        self.type = Type
        self.attack = int(Attack)
        self.defense = int(Defense)
        self.hp = int(HealthPoints)
        self.sp = int(StaminaPoints)


    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_stats(self,index):
        stats = [self.attack, self.defense, self.hp, self.sp]
        return stats[index]

    def __str__(self):
        return self.name + "(" + self.type + ")" + "Attack: " + str(self.attack) + "Defense: " + str(self.defense) + "HP: " + str(self.hp) + "SP: " + str(self.sp)


class Team:
    def __init__(self, filename):
        self.characters = []
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                character = Character(*data)
                self.characters.append(character)

    def get_member(self, index):
        return self.characters[index]

    def __str__(self):
        result = ""
        for character in self.characters:
            result += "----------\n" + str(character) + "\n"
        return result


def main():
    team = Team("saveData.csv")
    print("PRINTING ONE MEMBER ONLY:")
    print(team.get_member(0))
    print()
    print("PRINTING WHOLE TEAM:")
    print(team)
