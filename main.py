from window import Window
from line import Line
from point import Point
from cell import Cell

my_window = Window(800, 800)
while True:
    point_one = input("enter top left points in x,y format")
    point_one = Point(point_one.split(",")[0], point_one.split(",")[1])
    point_two = input("enter bottom right points in x,y format")
    point_two = Point(point_two.split(",")[0], point_two.split(",")[1])
    my_cell = Cell(my_window)
    my_cell.draw(point_one, point_two)
    leave = input("again?(Y/n)")
    if leave == "n":
        break
my_window.wait_for_close()
