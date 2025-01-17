from tkinter import Tk, BOTH, Canvas
from maze import Maze
from cell import Cell
from point import Point


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze_Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.update_idletasks()
        print(self.__root.geometry())
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self._canvas.pack(fill="both", expand=True)
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

    def redraw(self):
        # this whole method is not needed if mainloop() is implimented
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        # self.__root.mainloop() (this is better if I don't end up adding to the loop)
        self.running = True
        while self.running:
            point_one = input("enter top left point for maze in x,y format: ")
            point_one = Point(point_one.split(",")[0], point_one.split(",")[1])
            cell_size_x = input("enter cell size x: ")
            cell_size_y = input("enter cell size y: ")
            num_cols = input("enter num of cols: ")
            num_rows = input("enter num of rows: ")
            maze = Maze(point_one, cell_size_x, cell_size_y, num_cols, num_rows, self)
            print(maze._cells)
            leave = input("again?(Y/n)")
            if leave == "n":
                self.close()
            self.redraw()

    def close(self):
        self.running = False
        self.__root.destroy()
