from window import Window
from maze import Maze

top_left_x = 30
top_left_y = 30

# modify the variables below to change the maze structure
cell_size_x = 40
cell_size_y = 30
num_cols = 30
num_rows = 30

my_window = Window(cell_size_x * num_cols + 40, cell_size_y * num_rows + 40)
maze = Maze(
    top_left_x,
    top_left_y,
    cell_size_x,
    cell_size_y,
    num_cols,
    num_rows,
    my_window
)
my_window.wait_for_close()
