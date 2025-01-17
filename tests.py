import unittest
from point import Point
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        start_point = Point(0, 0)
        maze = Maze(start_point, 1, 1, num_cols, num_rows, seed=0)
        self.assertEqual(
            len(maze._cells),
            num_rows
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_cols
        )

    def test_maze_create_cells_alt(self):
        num_cols = 79
        num_rows = 32
        start_point = Point(0, 0)
        maze = Maze(start_point, 1, 1, num_cols, num_rows, seed=0)
        self.assertEqual(
            len(maze._cells),
            num_rows
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_cols
        )

    def test_maze_create_cells_one(self):
        num_cols = 1
        num_rows = 1
        start_point = Point(0, 0)
        maze = Maze(start_point, 1, 1, num_cols, num_rows, seed=0)
        self.assertEqual(
            len(maze._cells),
            num_rows
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_cols
        )

    def test_enter_and_exit_breaks(self):
        num_cols = 5
        num_rows = 7
        start_point = Point(0, 0)
        maze = Maze(start_point, 1, 1, num_cols, num_rows, seed=0)
        self.assertEqual(
            maze._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            maze._cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False
        )

    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 7
        start_point = Point(0, 0)
        maze = Maze(start_point, 1, 1, num_cols, num_rows, seed=0)
        for row in maze._cells:
            for cell in row:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()
