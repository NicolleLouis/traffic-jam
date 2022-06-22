from typing import TYPE_CHECKING, Optional

from services.data_storage.road import RoadDataStorageService
from services.road.road_car_arrived import RoadCarArrivedService
from services.road.road_car_random_creation import RoadCarRandomCreationService
from services.road.road_position_generator import RoadPositionGenerator

if TYPE_CHECKING:
    from models import Grid, Position, TrafficLight, Car


class Road:
    def __init__(self, grid: 'Grid', x=None, y=None):
        self.positions: list['Position'] = RoadPositionGenerator.generate_straight_line(
            grid=grid,
            x=x,
            y=y,
        )
        self.grid = grid
        self.cars: list['Car'] = []
        self.traffic_lights: list['TrafficLight'] = []
        self.car_joining_road = 0
        self.car_leaving_road = 0

        self.car_arrived_service = RoadCarArrivedService(self)
        self.car_creation_service = RoadCarRandomCreationService(self)
        self.data_storage = RoadDataStorageService(self)

    def step(self) -> None:
        for traffic_light in self.traffic_lights:
            traffic_light.step()
        self.car_creation_service.generate_car()
        self.car_arrived_service.remove_car_on_last_position()

    def add_car(self, car: 'Car') -> None:
        self.cars.append(car)
        self.car_joining_road += 1

    def remove_car(self, car: 'Car') -> None:
        self.cars.remove(car)
        self.car_leaving_road += 1
        self.data_storage.add_car_travel_time(car)

    def add_traffic_light(self, traffic_light: 'TrafficLight') -> None:
        self.traffic_lights.append(traffic_light)

    def get_traffic_light(self, position: 'Position') -> Optional['TrafficLight']:
        for traffic_light in self.traffic_lights:
            if traffic_light.position == position:
                return traffic_light
        return None

    def next_position(self, position: 'Position') -> 'Position':
        for index, potential_position in enumerate(self.positions):
            if position == potential_position:
                try:
                    return self.positions[index + 1]
                except IndexError:
                    raise Exception("Last position of road")
        raise Exception("Position not in road")

    def is_position_on_road(self, position: 'Position') -> bool:
        for potential_position in self.positions:
            if position == potential_position:
                return True
        return False
