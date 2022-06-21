class Grid:
    def __init__(self, size=50):
        self.width = size
        self.length = size
        self.objects = []

    def add_object(self, grid_object):
        self.objects.append(grid_object)

    def is_position_empty(self, position):
        for grid_object in self.objects:
            if grid_object.position == position:
                return False
        return True
