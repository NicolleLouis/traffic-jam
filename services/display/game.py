from typing import TYPE_CHECKING

from services.display.grid import GridDisplayService
from services.display.road import RoadDisplayService

if TYPE_CHECKING:
    from models import Game


class GameDisplayService:
    def __init__(self, game: 'Game'):
        self.game: 'Game' = game

    def display_information(
            self,
            display_road=False,
            display_grid=True,
            road_display_context=False,
            road_display_car=False,
            road_display_traffic_light=False,
    ):
        if display_road:
            self.display_road_data(
                road_display_context=road_display_context,
                road_display_car=road_display_car,
                road_display_traffic_light=road_display_traffic_light,
            )
        if display_grid:
            self.display_grid()

    def display_road_data(
            self,
            road_display_context=False,
            road_display_car=False,
            road_display_traffic_light=False,
    ):
        print("Roads Data:")
        print(f"Roads Number: {len(self.game.roads)}")
        for index, road in enumerate(self.game.roads):
            print("#####")
            print(f"Road Number {index}:")
            RoadDisplayService(road).display_data(
                display_context=road_display_context,
                display_car=road_display_car,
                display_traffic_light=road_display_traffic_light,
            )

    def display_grid(self):
        GridDisplayService(self.game.grid).display_grid()