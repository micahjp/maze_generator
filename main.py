from window import Window
from maze import Maze

my_window = Window(940, 940)
maze = Maze(30, 30, 30, 30, 30, 30, my_window)
my_window.wait_for_close()
