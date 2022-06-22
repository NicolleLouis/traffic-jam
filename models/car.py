from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from models import Grid, Position, Road

from constants.traffic_light_state import TrafficLightState


class Car:
    def __init__(self, road: 'Road', position: 'Position'):
        self.road: 'Road' = road
        self.grid: 'Grid' = self.road.grid
        self.position: 'Position' = position

        self.grid.add_object(self)
        self.road.add_car(self)

    def step(self) -> None:
        if self.is_traffic_light_blocking():
            return
        next_position = self.next_position()
        if not self.can_move(next_position):
            return
        self.move(next_position)

    def can_move(self, position: 'Position') -> bool:
        return self.grid.is_position_empty(position)

    def move(self, next_position) -> None:
        self.position = next_position

    def next_position(self) -> 'Position':
        return self.road.next_position(self.position)

    def is_traffic_light_blocking(self) -> bool:
        traffic_light = self.road.get_traffic_light(self.position)
        if traffic_light is None:
            return False
        else:
            if traffic_light.state in [TrafficLightState.Green, TrafficLightState.Yellow]:
                return False
        return True
