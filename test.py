from models import Grid, Road
from models.position import Position

grid = Grid(10)
road = Road(grid=grid, x=None, y=4)
road.display_data()
print(road.next_position(Position(9, 5)))
