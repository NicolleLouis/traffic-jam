from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Grid

from models import Position


class GridDisplay:
    def __init__(self, grid: 'Grid'):
        self.grid: 'Grid' = grid

    def display_grid(self):
        for y in range(self.grid.height):
            self.display_line(y=y)

    def display_line(self, y):
        line_representation = ""
        for x in range(self.grid.width):
            position = Position(x=x, y=y)
            if self.grid.is_position_empty(position):
                line_representation += " "
            else:
                line_representation += "#"
        print(line_representation)
