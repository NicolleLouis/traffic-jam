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

    def add_car(self, car):
        self.cars.append(car)

    def next_position(self, position):
        for index, potential_position in enumerate(self.positions):
            if position == potential_position:
                try:
                    return self.positions[index + 1]
                except IndexError:
                    raise Exception("Last position of road")
        raise Exception("Position not in road")

    def display_data(self, display_context=False):
        if display_context:
            self.display_context()
        self.display_car()

    def display_context(self):
        print(f"Road Length: {len(self.positions)}")
        for position in self.positions:
            print(position)

    def display_car(self):
        print(f"Car number: {len(self.cars)}")
        for index, car in enumerate(self.cars):
            print(f"Car {index}: {car.position}")
