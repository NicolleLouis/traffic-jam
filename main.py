from constants.traffic_light_state import TrafficLightState
from models import Road, TrafficLight
from models.game import Game

game = Game(verbose=False)
game.add_road(Road(grid=game.grid, x=4))
game.add_road(Road(grid=game.grid, y=4))

TrafficLight(
    road=game.roads[0],
    position=game.roads[0].positions[3]
)
TrafficLight(
    road=game.roads[1],
    position=game.roads[0].positions[3],
    initial_state=TrafficLightState.Red
)

game.run(number_of_turns=1000)
