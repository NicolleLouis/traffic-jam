from typing import TYPE_CHECKING

from services.probability import ProbabilityService

if TYPE_CHECKING:
    from models import Road

from models import Car


class RoadCarRandomCreationService:
    def __init__(self, road: 'Road', probability=33):
        self.road: 'Road' = road
        self.start_position = self.first_road_position()
        self.probability = probability

    def generate_car(self) -> None:
        if not ProbabilityService.percentage_roll(self.probability):
            return

        if not self.road.grid.is_position_empty(self.start_position):
            return

        Car(
            road=self.road,
            position=self.start_position
        )

    def first_road_position(self):
        return self.road.positions[1]
