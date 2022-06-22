from constants.traffic_light_state import TrafficLightState
from models import Road, Car, TrafficLight
from models.game import Game

game = Game()
game.add_road(Road(grid=game.grid, x=4))
game.add_road(Road(grid=game.grid, y=4))
Car(
    grid=game.grid,
    road=game.roads[0],
    position=game.roads[0].positions[0]
)
Car(
    grid=game.grid,
    road=game.roads[0],
    position=game.roads[0].positions[1]
)
Car(
    grid=game.grid,
    road=game.roads[1],
    position=game.roads[1].positions[0]
)
Car(
    grid=game.grid,
    road=game.roads[1],
    position=game.roads[1].positions[1]
)

TrafficLight(
    road=game.roads[0],
    position=game.roads[0].positions[3]
)

TrafficLight(
    road=game.roads[1],
    position=game.roads[0].positions[3],
    initial_state=TrafficLightState.Red
)

game.run(number_of_turns=20, verbose=True)
