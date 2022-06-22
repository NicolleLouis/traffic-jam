from typing import TYPE_CHECKING

from constants.traffic_light_state import TrafficLightState

if TYPE_CHECKING:
    from models import Road


class TrafficLight:
    def __init__(
            self,
            road: 'Road',
            position,
            initial_state=TrafficLightState.Green
    ):
        self.position = position
        road.add_traffic_light(self)
        self.state = initial_state
        self.last_change = 0
        self.green_period = 1
        self.yellow_period = 0
        self.red_period = 2

    def step(self):
        if self.state == TrafficLightState.Green and self.last_change == self.green_period:
            self.state = TrafficLightState.Yellow
            self.last_change = 0
        elif self.state == TrafficLightState.Yellow and self.last_change == self.yellow_period:
            self.state = TrafficLightState.Red
            self.last_change = 0
        elif self.state == TrafficLightState.Red and self.last_change == self.red_period:
            self.state = TrafficLightState.Green
            self.last_change = 0
        else:
            self.last_change += 1

    def display_data(self):
        print(
            f"Traffic Light on {self.position} "
            f"has state: {self.state.value}"
        )
