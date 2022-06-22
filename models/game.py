from models import Grid, Road
from services.display.game import GameDisplayService


class Game:
    def __init__(self):
        self.grid = Grid(size=10)
        self.roads = []
        self.display_service = GameDisplayService(self)

    def add_road(self, road: 'Road'):
        self.roads.append(road)

    def step(self):
        for grid_object in self.grid.objects:
            grid_object.step()
        for road in self.roads:
            road.step()

    def run(self, number_of_turns=10):
        for turn_number in range(number_of_turns):
            print(f"Turn Number: {turn_number}")
            self.display_service.display_information(
                display_road=True,
                road_display_traffic_light=True,
            )
            self.step()
