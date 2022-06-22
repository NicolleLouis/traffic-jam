from typing import TYPE_CHECKING

from models.position import Position

if TYPE_CHECKING:
    from models import Grid


class RoadPositionGenerator:
    @staticmethod
    def check_data_validity(grid: 'Grid', x=None, y=None):
        size = grid.width
        if x is None and y is None:
            raise Exception('Road should have 1 axis')
        if x is not None and y is not None:
            raise Exception('Road should have at most 1 axis')
        if x is not None:
            if x < 0 or x >= size:
                raise Exception("Axis outside the grid")
        if y is not None:
            if y < 0 or y >= size:
                raise Exception("Axis outside the grid")

    @staticmethod
    def generate_straight_line(grid: 'Grid', x=None, y=None, reverse=False):
        road_positions = []
        size = grid.width
        RoadPositionGenerator.check_data_validity(grid=grid, x=x, y=y)
        if y is not None:
            road_positions = list(
                map(
                    lambda new_x: Position(new_x, y),
                    range(size)
                )
            )
        if x is not None:
            road_positions = list(
                map(
                    lambda new_y: Position(x, new_y),
                    range(size)
                )
            )
        road_positions.reverse()
        return road_positions
