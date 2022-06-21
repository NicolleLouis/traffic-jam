class Car:
    def __init__(self, road, grid, position):
        self.road = road
        self.grid = grid
        self.position = position

        self.grid.add_object(self)
        self.road.add_car(self)

    def step(self):
        self.move()

    def move(self):
        try:
            next_position = self.road.next_position(self.position)
        except Exception as exception:
            print(exception)
            return
        if self.grid.is_position_empty(next_position):
            self.position = next_position
