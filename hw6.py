
class Animal:
    def __init__(self, public_name, common_name, scientific_name, characteristics, display):
        self.public_name = public_name
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.characteristics = characteristics
        self.display = display


class Characteristics:
    def __init__(self, height, weight, age, primary_color, secondary_color):
        self.height = height
        self.weight = weight
        self.age = age
        self.primary_color = primary_color
        self.secondary_color = secondary_color


class Display:
    def __init__(self, arrival_date, building_number, special_diet, display_number, no_show_start, no_show_end):
        self.arrival_date = arrival_date
        self.building_number = building_number
        self.special_diet = special_diet
        self.display_number = display_number
        self.no_show_start = no_show_start
        self.no_show_end = no_show_end

import csv

def main(input_file):
    animals = {}
    file = open(input_file, 'r')
    with open(input_file) as file:
        header = file.readline().strip().split(",")
        for line in file:
            data = line.strip().split(",")
            animal_id = int(data[0])
            public_name = data[1]
            common_name = data[2]
            scientific_name = data[3]
            weight = float(data[4])
            height = float(data[5])
            age = int(data[6])
            primary_color = data[7]
            secondary_color = data[8]
            arrival_date = data[9]
            building_num = int(data[10])
            special_diet = data[11] == "true"
            no_show_start = data[12]
            no_show_end = data[13]

            characteristics = Characteristics(height, weight, age, primary_color, secondary_color)
            display = Display(arrival_date, building_num, special_diet, display_num, no_show_start, no_show_end)
            animal = Animal(public_name, common_name, scientific_name, characteristics, display)

            animals[animal_id] = animal

    return animals


def report_animal_types(output_file):
    animal_types = {}
    for animal in animals.values():
        common_name = animal.common_name
        scientific_name = animal.scientific_name
        if (common_name, scientific_name) in animal_types:
            animal_types[(common)]


