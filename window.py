from tkinter import Tk, BOTH, Canvas
from maze import Maze
from cell import Cell
from point import Point


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze_Solver")
        self.__root.geometry(f"{width+50}x{height+13}")
        self.__root.update_idletasks()
        print(self.__root.geometry())
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self._canvas.pack(fill="both", expand=True)
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.__root.destroy()
