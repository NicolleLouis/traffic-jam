from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Road, Car


class RoadDataStorageService:
    def __init__(self, road: 'Road'):
        self.road: 'Road' = road
        self.car_travel_time: list[int] = []

    def add_car_travel_time(self, car: 'Car'):
        self.car_travel_time.append(car.time_traveled)

    def average_travel_time(self):
        if len(self.car_travel_time) == 0:
            return None
        return sum(self.car_travel_time) / len(self.car_travel_time)

    def display_car_travel_time(self, verbose=False):
        if verbose:
            print("Raw data:")
            print(self.car_travel_time)
        print(f"Number of car analysed: {len(self.car_travel_time)}")
        print(f"Fastest: {min(self.car_travel_time)}")
        print(f"Slowest: {max(self.car_travel_time)}")
        print(f"Average: {self.average_travel_time()}")
