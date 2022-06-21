from models import Grid, Road

grid = Grid(10)
road = Road(grid=grid, x=None, y=10)
for position in road.positions:
    print(position)
