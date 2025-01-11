from time import sleep
from cell import Cell
from point import Point


class Maze():
    def __init__(
            self,
            top_left_point,
            cell_size_x,
            cell_size_y,
            num_cols,
            num_rows,
            window
            ):
        self._cells = None
        self.top_left_point = top_left_point
        self.cell_size_x = int(cell_size_x)
        self.cell_size_y = int(cell_size_y)
        self.num_cols = int(num_cols)
        self.num_rows = int(num_rows)
        self.window = window
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for row in range(self.num_rows):
            self._cells.append([])
            for column in range(self.num_cols):
                self._cells[row].append(Cell(self.window))
                self._draw_cell(self._cells[row][column], row, column)

    def _draw_cell(self, cell, row, column):
        cell_top_left = Point(column * self.cell_size_x, row * self.cell_size_y) + self.top_left_point
        cell_bottom_right = Point(cell_top_left.x + self.cell_size_x, cell_top_left.y + self.cell_size_y)
        cell.draw(
                cell_top_left,
                cell_bottom_right
                )
        self._animate()

    def _animate(self):
        self.window.redraw()
        sleep(0.05)
