from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# maze0.svg
# 0 is passable, 1 is wall
# https://juliannorton.github.io/keep-talking-bomb-defusal-manual/img/maze0.svg

solution = []

# TODO, add multiple mazes and 'circle' locations to select the maze 
matrix = [
    [0,0,0,0,0,1,0,0,0,0,0],
    [0,1,1,1,0,1,0,1,1,1,1],
    [0,1,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,1,0,0,0,0,0],
    [0,1,1,1,0,1,0,1,1,1,0],
    [0,1,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,1,0],
    [0,1,1,1,0,1,0,1,1,1,0],
    [0,0,0,1,0,0,0,1,0,0,0]
]

grid = Grid(matrix=matrix)

# TODO, add user input for current location and destination
# Currently locations are hard-coded
start = grid.node(0, 0)
end = grid.node(10, 10)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

# Solution debugging
def debug_maze():
    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))
    print('path')

# Converts grid notation to KTANE maze size
for i in range(len(path)):
    if i%2 == 0:
        solution.append(path[i])

# Converts solution notation to cardinal direction
def which_direction(solution):
    solution_direction = []
    for i in range(len(solution)-1):
        current_location = solution[i]
        next_location = solution[i+1]
        if current_location[0] < next_location[0]:
            print('move right!')
        elif current_location[0] > next_location[0]:
            print('move left!')
        elif current_location[1] < next_location[1]:
            print('move down!')
        elif current_location[1] > next_location[1]:
            print('move up!')
        else:
            'something went wrong'

which_direction(solution)
