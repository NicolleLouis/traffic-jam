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

    def display_data(
            self,
            display_context=False,
            display_car=False,
            display_traffic_light=False,
    ):
        if display_context:
            self.display_context()
        if display_car:
            self.display_car()
        if display_traffic_light:
            self.display_traffic_light()

    def display_context(self):
        print(f"Road Length: {len(self.positions)}")
        for position in self.positions:
            print(position)

    def display_car(self):
        print(f"Car number: {len(self.cars)}")
        for index, car in enumerate(self.cars):
            print(f"Car {index}: {car.position}")

    def display_traffic_light(self):
        print(f"Traffic light number: {len(self.traffic_lights)}")
        for traffic_light in self.traffic_lights:
            traffic_light.display_data()
