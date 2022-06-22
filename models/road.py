from typing import TYPE_CHECKING

from services.road_position_generator import RoadPositionGenerator

if TYPE_CHECKING:
    from models import Grid


class Road:
    def __init__(self, grid: 'Grid', x=None, y=None):
        self.positions = RoadPositionGenerator.generate_straight_line(
            grid=grid,
            x=x,
            y=y,
        )
        self.cars = []
        self.traffic_lights = []

    def step(self):
        for traffic_light in self.traffic_lights:
            traffic_light.step()

    def add_car(self, car):
        self.cars.append(car)

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    def next_position(self, position):
        for index, potential_position in enumerate(self.positions):
            if position == potential_position:
                try:
                    return self.positions[index + 1]
                except IndexError:
                    raise Exception("Last position of road")
        raise Exception("Position not in road")

    def is_position_on_road(self, position):
        for potential_position in self.positions:
            if position == potential_position:
                return True
        return False
