from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze_Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.update_idletasks()
        print(self.__root.geometry())
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self.__root, width=width, height=height)
        self._canvas.pack()
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
            self.redraw()

    def close(self):
        self.running = False
        self.__root.destroy()
