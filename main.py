from constants.traffic_light_state import TrafficLightState
from models import Road, TrafficLight
from models.game import Game

game = Game(size=20)
h1 = Road(grid=game.grid, x=5)
h2 = Road(grid=game.grid, x=10)
h3 = Road(grid=game.grid, x=15)
v1 = Road(grid=game.grid, y=5)
v2 = Road(grid=game.grid, y=10)
v3 = Road(grid=game.grid, y=15)

roads = [h1, h2, h3, v1, v2, v3]
for road in roads:
    game.add_road(road)

# TrafficLight(
#     road=game.roads[0],
#     position=game.roads[0].positions[3]
# )
# TrafficLight(
#     road=game.roads[1],
#     position=game.roads[1].positions[3],
#     initial_state=TrafficLightState.Red
# )

game.run(number_of_turns=1000)
