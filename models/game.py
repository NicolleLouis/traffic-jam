from models import Grid, Road
from services.display.game import GameDisplayService


class Game:
    def __init__(self, verbose=False):
        self.grid = Grid(size=10)
        self.roads = []
        self.display_service = GameDisplayService(self)
        self.verbose = verbose

    def run(self, number_of_turns=10) -> None:
        for turn_number in range(number_of_turns):
            if self.verbose:
                self.display_service.display_information(
                    turn_number=turn_number,
                    display_road=False,
                    road_display_traffic_light=False,
                )
            self.step()
        self.conclude()

    def step(self) -> None:
        for road in self.roads:
            road.step()
        for grid_object in self.grid.objects:
            grid_object.step()

    def conclude(self):
        self.display_service.display_final_data()

    def add_road(self, road: 'Road'):
        self.roads.append(road)
