from models import Grid, Road


class Game:
    def __init__(self):
        self.grid = Grid(size=10)
        self.roads = []

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
            self.display_information(
                display_road=True,
                road_display_traffic_light=True,
            )
            self.step()

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
        print(f"Roads Number: {len(self.roads)}")
        for index, road in enumerate(self.roads):
            print("#####")
            print(f"Road Number {index}:")
            road.display_data(
                display_context=road_display_context,
                display_car=road_display_car,
                display_traffic_light=road_display_traffic_light,
            )

    def display_grid(self):
        self.grid.display_grid()
