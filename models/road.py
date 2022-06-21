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
