from models import Grid, Road
from models.car import Car


class Game:
    def __init__(self):
        self.grid = Grid(size=10)
        self.roads = [
            Road(grid=self.grid, x=4),
            Road(grid=self.grid, y=4),
        ]
        Car(
            grid=self.grid,
            road=self.roads[0],
            position=self.roads[0].positions[0]
        )
        Car(
            grid=self.grid,
            road=self.roads[0],
            position=self.roads[0].positions[1]
        )
        Car(
            grid=self.grid,
            road=self.roads[1],
            position=self.roads[1].positions[0]
        )
        Car(
            grid=self.grid,
            road=self.roads[1],
            position=self.roads[1].positions[1]
        )

    def step(self):
        for grid_object in self.grid.objects:
            grid_object.step()

    def run(self, number_of_turns=10):
        for turn_number in range(number_of_turns):
            print(f"Turn Number: {turn_number}")
            self.display_information()
            self.step()

    def display_information(self, display_road=False):
        if display_road:
            self.display_road_data()
        self.display_grid()

    def display_road_data(self):
        print("Roads Data:")
        print(f"Roads Number: {len(self.roads)}")
        for index, road in enumerate(self.roads):
            print("#####")
            print(f"Road Number {index}:")
            road.display_data()

    def display_grid(self):
        self.grid.display_grid()
