from typing import TYPE_CHECKING

from services.display.data_storage.road import RoadDataDisplay

if TYPE_CHECKING:
    from models import Road


class RoadDisplay:
    def __init__(self, road: 'Road'):
        self.road: 'Road' = road

    def display_data(
            self,
            display_context=False,
            display_car=False,
            display_traffic_light=False,
    ):
        if display_context:
            self.display_context()
        if display_car:
            self.display_car()
        if display_traffic_light:
            self.display_traffic_light()

    def display_final_data(self, verbose=False):
        if verbose:
            print(f'Cars created: {self.road.car_joining_road}')
            print(f'Cars arrived: {self.road.car_leaving_road}')
        self.display_car_travel_time()

    def display_context(self):
        print(f"Road Length: {len(self.road.positions)}")
        for position in self.road.positions:
            print(position)

    def display_car(self):
        print(f"Car number: {len(self.road.cars)}")
        for index, car in enumerate(self.road.cars):
            print(f"Car {index}: {car.position}")

    def display_traffic_light(self):
        print(f"Traffic light number: {len(self.road.traffic_lights)}")
        for traffic_light in self.road.traffic_lights:
            traffic_light.display_data()

    def display_car_travel_time(self):
        RoadDataDisplay(self.road.data_storage).display_car_travel_time()
