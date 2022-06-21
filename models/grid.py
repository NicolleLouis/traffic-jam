from models import Position


class Grid:
    def __init__(self, size=50):
        self.width = size
        self.height = size
        self.objects = []

    def add_object(self, grid_object):
        self.objects.append(grid_object)

    def is_position_empty(self, position):
        for grid_object in self.objects:
            if grid_object.position == position:
                return False
        return True

    def display_grid(self):
        for y in range(self.height):
            self.display_line(y=y)

    def display_line(self, y):
        line_representation = ""
        for x in range(self.width):
            position = Position(x=x, y=y)
            if self.is_position_empty(position):
                line_representation += " "
            else:
                line_representation += "#"
        print(line_representation)
