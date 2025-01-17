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
        self.visited = False

    def __repr__(self):
        return f"Cell({self.top_left_point.x}, {self.top_left_point.y})" if self.top_left_point else "Cell()"

    def draw(self, top_left_point, bottom_right_point):
        self.top_left_point = top_left_point
        self.top_right_point = Point(bottom_right_point.x, top_left_point.y)
        self.bottom_right_point = bottom_right_point
        self.bottom_left_point = Point(top_left_point.x, bottom_right_point.y)
        self.center_point = self.top_left_point + ((self.bottom_right_point - self.top_left_point) / 2)
        self.top_wall = Line(self.top_left_point, self.top_right_point)
        self.right_wall = Line(self.top_right_point, self.bottom_right_point)
        self.bottom_wall = Line(self.bottom_right_point, self.bottom_left_point)
        self.left_wall = Line(self.bottom_left_point, self.top_left_point)

        fill_color = "black" if self.has_top_wall else "white"
        self._window.draw_line(self.top_wall, fill_color)

        fill_color = "black" if self.has_right_wall else "white"
        self._window.draw_line(self.right_wall, fill_color)

        fill_color = "black" if self.has_bottom_wall else "white"
        self._window.draw_line(self.bottom_wall, fill_color)

        fill_color = "black" if self.has_left_wall else "white"
        self._window.draw_line(self.left_wall, fill_color)

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"
        self.move = Line(self.center_point, to_cell.center_point)
        self._window.draw_line(self.move, fill_color)
