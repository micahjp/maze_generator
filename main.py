from window import Window
from line import Line
from point import Point

my_window = Window(800, 500)
point_one = Point(50, 50)
point_two = Point(150, 150)
my_window.draw_line(Line(point_one, point_two), "red")
my_window.wait_for_close()
