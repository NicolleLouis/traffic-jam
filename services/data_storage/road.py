from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Road, Car


class RoadDataStorage:
    def __init__(self, road: 'Road'):
        self.road: 'Road' = road
        self.car_travel_time: list[int] = []

    def add_car_travel_time(self, car: 'Car'):
        self.car_travel_time.append(car.time_traveled)

    def prepare_data(self) -> None:
        pass
