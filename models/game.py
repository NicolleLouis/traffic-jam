from models import Grid, Road


class Game:
    def __init__(self):
        self.grid = Grid(size=10)
        self.roads = [
            Road(grid=self.grid, x=4),
            Road(grid=self.grid, y=4)
        ]

    def display_information(self):
        self.display_road_data()

    def display_road_data(self):
        print("Roads Data:")
        print(f"Roads Number: {len(self.roads)}")
        for index, road in enumerate(self.roads):
            print("#####")
            print(f"Road Number {index}:")
            road.display_data()
