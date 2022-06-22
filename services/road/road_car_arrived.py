from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Road


class RoadCarArrivedService:
    def __init__(self, road: 'Road'):
        self.road: 'Road' = road
        self.finish_position = self.last_road_position()

    def remove_car_on_last_position(self):
        for car in self.road.cars:
            if car.position == self.finish_position:
                self.road.remove_car(car)
                self.road.grid.remove_object(car)

    def last_road_position(self):
        return self.road.positions[-1]
