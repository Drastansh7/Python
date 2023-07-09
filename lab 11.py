class Bird:
    def __init__(self, weightinkg, name, type, can_flock):
        self.weightinkg = weightinkg
        self.name = name
        self.type = type
        self.can_flock = can_flock

    def __str__(self):
        return f"{self.name} ({self.type}), {self.weightinkg} kg, flocking: {self.can_flock}"

    def get_weightinkg(self):
        return self.weightinkg

    def set_weightinkg(self, weightinkg):
        self.weightinkg = weightinkg

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def can_flock(self):
        return self.can_flock

    def set_can_flock(self, can_flock):
        self.can_flock = can_flock

from Bird import Bird

class FlightlessBird(Bird):
    def __init__(self, weightinkg, name, type, can_flock, max_run_speed):
        super().__init__(weightinkg, name, type, can_flock)
        self.max_run_speed = max_run_speed

    def __str__(self):
        return f"{super().__str__()}, max run speed: {self.max_run_speed} km/h"

    def get_max_run_speed(self):
        return self.max_run_speed

    def set_max_run_speed(self, max_run_speed):
        self.max_run_speed = max_run_speed

    def run(self, minutes):

        distance = self.max_run_speed * (minutes / 60)
        return distance

from Bird import Bird

class FlightedBird(Bird):
    def __init__(self, weightinkg, name, type, can_flock, max_flight_speed):
        super().__init__(weightinkg, name, type, can_flock)
        self.max_flight_speed = max_flight_speed

    def __str__(self):
        return f"{super().__str__()}, max flight speed: {self.max_flight_speed} km/h"

    def get_max_flight_speed(self):
        return self.max_flight_speed

    def set_max_flight_speed(self, max_flight_speed):
        self.max_flight_speed = max_flight_speed

    def fly(self, minutes):

        distance = self.max_flight_speed * (minutes / 60)
        return distance

from Bird import Bird
from FlightlessBird import FlightlessBird
from FlightedBird import FlightedBird

def main():

    bird1 = Bird(2.5, "Chickadee", "Songbird", True)
    bird2 = Bird(1.1, "Mallard", "Duck", True)

    flightless_bird1 = FlightlessBird(120, "Ostrich", "Ratite", False, 70)
    flightless_bird2 = FlightlessBird(20, "Emu", "Ratite", False, 55)

    flighted_bird1 = FlightedBird(0
