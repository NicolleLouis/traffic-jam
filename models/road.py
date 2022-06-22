from typing import TYPE_CHECKING, Optional

from services.road_position_generator import RoadPositionGenerator

if TYPE_CHECKING:
    from models import Grid, Position, TrafficLight, Car


class Road:
    def __init__(self, grid: 'Grid', x=None, y=None):
        self.positions: list['Position'] = RoadPositionGenerator.generate_straight_line(
            grid=grid,
            x=x,
            y=y,
        )
        self.cars: list['Car'] = []
        self.traffic_lights: list['TrafficLight'] = []

    def step(self) -> None:
        for traffic_light in self.traffic_lights:
            traffic_light.step()

    def add_car(self, car: 'Car') -> None:
        self.cars.append(car)

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
