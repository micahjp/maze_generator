from line import Line
from point import Point


class Cell():
    def __init__(
            self,
            window
            ):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._window = window

    def draw(self, top_left, bottom_right):
        self.top_left = top_left
        self.top_right = Point(bottom_right.x, top_left.y)
        self.bottom_right = bottom_right
        self.bottom_left = Point(top_left.x, bottom_right.y)
        print(f"top left = {self.top_left.x},{self.top_left.y}")
        print(f"top right = {self.top_right.x},{self.top_right.y}")
        print(f"bottom right = {self.bottom_right.x},{self.bottom_right.y}")
        print(f"bottom left = {self.bottom_left.x},{self.bottom_left.y}")
        if self.has_top_wall:
            self.top_wall = Line(self.top_left, self.top_right)
            self.top_wall = self._window.draw_line(self.top_wall, "black")
        if self.has_right_wall:
            self.right_wall = Line(self.top_right, self.bottom_right)
            self.right_wall = self._window.draw_line(self.right_wall, "black")
        if self.has_bottom_wall:
            self.bottom_wall = Line(self.bottom_right, self.bottom_left)
            self.bottom_wall = self._window.draw_line(self.bottom_wall, "black")
        if self.has_left_wall:
            self.left_wall = Line(self.bottom_left, self.top_left)
            self.left_wall = self._window.draw_line(self.left_wall, "black")
