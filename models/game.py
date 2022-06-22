from models import Grid, Road
from services.display.game import GameDisplayService


class Game:
    def __init__(self):
        self.grid = Grid(size=10)
        self.roads = []
        self.display_service = GameDisplayService(self)

    def add_road(self, road: 'Road'):
        self.roads.append(road)

    def step(self) -> None:
        for road in self.roads:
            road.step()
        for grid_object in self.grid.objects:
            grid_object.step()

    def run(self, number_of_turns=10, verbose=False) -> None:
        for turn_number in range(number_of_turns):
            if verbose:
                self.display_service.display_information(
                    turn_number=turn_number,
                    display_road=False,
                    road_display_traffic_light=False,
                )
            self.step()
