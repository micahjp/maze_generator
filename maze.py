import random
from time import sleep
from cell import Cell
from point import Point


class Maze():
    def __init__(
            self,
            top_left_x,
            top_left_y,
            cell_size_x,
            cell_size_y,
            num_cols,
            num_rows,
            window=None,
            seed=None
    ):
        self._cells = None
        self.top_left_point = Point(top_left_x, top_left_y)
        self.cell_size_x = int(cell_size_x)
        self.cell_size_y = int(cell_size_y)
        self.num_cols = int(num_cols)
        self.num_rows = int(num_rows)
        self.window = window
        self._create_cells()
        self._current_cell = self._cells[0][0]
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._current_cell = self._cells[0][0]
        self._current_cell_index = (0, 0)
        self.play_game(0, 0)

    def _create_cells(self):
        self._cells = []
        for row in range(self.num_rows):
            self._cells.append([])
            for column in range(self.num_cols):
                top_left_x = (column * self.cell_size_x) + \
                    self.top_left_point.x
                top_left_y = (row * self.cell_size_y) + self.top_left_point.y

                self._cells[row].append(
                    Cell(
                        self.window,
                        Point(top_left_x, top_left_y),
                        Point(
                            top_left_x + self.cell_size_x,
                            top_left_y + self.cell_size_y
                        )
                    )
                )
                if self.window:
                    self._draw_cell(self._cells[row][column])

    def _draw_cell(self, cell):
        cell.draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        sleep(0.001)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_rows - 1][self.num_cols -
                                       1].has_bottom_wall = False
        if self.window:
            self._draw_cell(self._cells[0][0])
            self._draw_cell(self._cells[self.num_rows - 1][self.num_cols - 1])

    def _break_walls_r(self, x, y):
        self._current_cell.visited = True
        directions = self._get_directions(x, y)

        while True:
            self._current_cell = self._cells[y][x]
            unvisited_neighbors = []
            for cell_x, cell_y in directions:
                if not self._cells[cell_y][cell_x].visited:
                    unvisited_neighbors.append((cell_x, cell_y))
            if not unvisited_neighbors:
                return

            target_cell_x, target_cell_y = unvisited_neighbors.pop(
                random.randrange(
                    0,
                    len(unvisited_neighbors)
                )
            )

            target_cell = self._cells[target_cell_y][target_cell_x]

            if target_cell_x < x:
                target_cell.has_right_wall = False
                self._current_cell.has_left_wall = False
            elif target_cell_x > x:
                target_cell.has_left_wall = False
                self._current_cell.has_right_wall = False
            elif target_cell_y < y:
                target_cell.has_bottom_wall = False
                self._current_cell.has_top_wall = False
            elif target_cell_y > y:
                target_cell.has_top_wall = False
                self._current_cell.has_bottom_wall = False

            if self.window:
                self._draw_cell(self._current_cell)
                self._draw_cell(target_cell)
            self._current_cell = target_cell
            self._break_walls_r(target_cell_x, target_cell_y)

    def _get_directions(self, x, y, validate=False):
        directions = []

        if validate:
            if x != 0 and not self._current_cell.has_left_wall:
                directions.append((x-1, y))
            if x != self.num_cols - 1 and not self._current_cell.has_right_wall:
                directions.append((x+1, y))
            if y != 0 and not self._current_cell.has_top_wall:
                directions.append((x, y-1))
            if y != self.num_rows - 1 and not self._current_cell.has_bottom_wall:
                directions.append((x, y+1))
        else:
            if x != 0:
                directions.append((x-1, y))
            if x != self.num_cols - 1:
                directions.append((x+1, y))
            if y != 0:
                directions.append((x, y-1))
            if y != self.num_rows - 1:
                directions.append((x, y+1))

        return directions

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _player_move(self, event, move):
        if self._current_cell == self._cells[self.num_rows-1][self.num_cols-1]:
            self.complete()
            self.window.close(game_complete=True)
        self._current_cell.visited = True
        move = tuple(a+b for a, b in zip(move, self._current_cell_index))
        valid_directions = self._get_directions(
            self._current_cell_index[0],
            self._current_cell_index[1],
            True
        )
        if move not in valid_directions:
            return
        previous_cell = self._current_cell
        self._current_cell = self._cells[move[1]][move[0]]
        self._current_cell_index = move

        if self.window and self._current_cell.visited:
            self._current_cell.draw_move(previous_cell, undo=True)
            previous_cell.visited = False
        else:
            self._current_cell.draw_move(previous_cell)
        return

    def play_game(self, x, y):
        self.window._canvas.bind(
                "<Left>",
                lambda event: self._player_move(event, (-1, 0))
            )
        self.window._canvas.bind(
                "<Down>",
                lambda event: self._player_move(event, (0, 1))
                )
        self.window._canvas.bind(
                "<Up>",
                lambda event: self._player_move(event, (0, -1))
            )
        self.window._canvas.bind(
                "<Right>",
                lambda event: self._player_move(event, (1, 0))
                )
        self.window._canvas.bind(
                "<KeyPress-h>",
                lambda event: self._player_move(event, (-1, 0))
            )
        self.window._canvas.bind(
                "<KeyPress-j>",
                lambda event: self._player_move(event, (0, 1))
                )
        self.window._canvas.bind(
                "<KeyPress-k>",
                lambda event: self._player_move(event, (0, -1))
            )
        self.window._canvas.bind(
                "<KeyPress-l>",
                lambda event: self._player_move(event, (1, 0))
                )
        self.window._canvas.bind(
                "<KeyPress-s>",
                self.solve
                )
        self.window._canvas.focus_set()
        return

    def solve(self, event=None):
        self._current_cell = self._cells[0][0]
        self._current_cell_index = (0, 0)
        self._reset_cells_visited()
        return self._solve_r(self._current_cell_index[0], self._current_cell_index[1])

    def _solve_r(self, x, y):
        if self._current_cell == self._cells[self.num_rows-1][self.num_cols-1]:
            self.complete()
            self.window.close(game_complete=True)
            return True
        self._current_cell.visited = True
        directions = self._get_directions(x, y, validate=True)

        while True:
            self._current_cell = self._cells[y][x]
            if not directions:
                return False
            target_x, target_y = directions.pop()
            previous_cell = self._cells[y][x]
            self._current_cell = self._cells[target_y][target_x]

            if self._current_cell.visited:
                continue

            if self.window:
                self._current_cell.draw_move(previous_cell, solve=True)
            if self._solve_r(target_x, target_y):
                return True
            if self.window:
                self._current_cell.draw_move(previous_cell, undo=True, solve=True)

    def complete(self):
        message_id = self.window._canvas.create_text(
            470,
            470,
            text="Maze Completed!",
            font=("Ariel", 40),
            fill="gold"
        )
        msg_loc = self.window._canvas.bbox(message_id)
        rect_id = self.window._canvas.create_rectangle(
            msg_loc[0],
            msg_loc[1],
            msg_loc[2],
            msg_loc[3],
            fill="white"
        )
        self.window._canvas.tag_lower(rect_id, message_id)
