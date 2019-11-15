"""Conway Game Of Life."""


import time


class Cell:
    """Cell class for holding one cell."""

    def __init__(self):
        """Initialize a cell."""
        self.neighbor_list = []
        self.current = False
        self.nextval = False

    def __str__(self):
        """Cast to a string."""
        if self.is_on():
            return "\N{full Block}"
        return " "

    def __repr__(self):
        """Representation."""
        if self.is_on():
            return "\N{full Block}"
        return " "

    def is_on(self):
        """Test current state."""
        return self.current

    def step(self):
        """Flip next value into place."""
        self.current = self.nextval

    def set_nextval(self):
        """Set the next value based on neighbor status."""
        count = 0
        for neighbor in self.neighbor_list:
            count += 1 if neighbor.is_on() else 0
        if count < 2:
            self.nextval = False
        elif count == 2:
            self.nextval = self.current
        elif count == 3:
            self.nextval = True
        else:
            self.nextval = False


class CellGrid:
    """Container grid of cells."""

    def __init__(self, rows=10, cols=10):
        """Build the grid."""
        self.rows, self.cols = rows, cols
        self.cell_grid = []

        for _ in range(self.rows + 2):
            col_list = []
            for col in range(self.cols + 2):
                col_list.append(Cell())
            self.cell_grid.append(col_list)

        for col_list in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                self.cell_grid[col_list][col].neighbor_list = [
                    self.cell_grid[col_list - 1][col],
                    self.cell_grid[col_list - 1][col - 1],
                    self.cell_grid[col_list - 1][col + 1],
                    self.cell_grid[col_list][col - 1],
                    self.cell_grid[col_list][col + 1],
                    self.cell_grid[col_list + 1][col],
                    self.cell_grid[col_list + 1][col - 1],
                    self.cell_grid[col_list + 1][col + 1],
                ]

    def setup(self, init_list):
        """Put initial values in place."""
        for row, col in init_list:
            self.cell_grid[row][col].current = True

    def show(self):
        """Display the grid."""
        time.sleep(.5)
        print(chr(27) + "[2j")
        print("\033c")
        print("\x1bc")
        for row in self.cell_grid:
            # print(row)
            for cell in row:
                print(cell, sep="", end="")
            print()

    def do_step(self):
        """Update next value then set it."""
        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                self.cell_grid[row][col].set_nextval()

        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                self.cell_grid[row][col].step()


def main():
    """Drive the exercise."""
    grid = CellGrid(30,30)

    grid.setup([[4, 5], [5, 5], [6, 5], [7, 6], [7, 7], [7, 8]])
    # grid.setup([[4, 5], [5, 5], [6, 5], [7, 5]])
    # grid.setup([[4, 5], [5, 5], [6, 5], [7, 5], [8,5]])
    # grid.setup([[4, 5], [4, 6], [5, 5], [5, 7], [6, 6], [6,7]])
    # grid.setup([[4, 5], [4, 6], [4, 7], [5, 5], [6, 6]])
    # grid.setup([[4, 5], [4, 6], [5, 5], [5, 5], [5, 7], [6, 6],[6, 7]])
    # grid.setup([[4, 5], [4, 6], [5, 4], [5, 7], [6, 5], [6, 6]])
    # grid.setup([[4, 5], [5, 4], [5, 6], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7]])
    # grid.setup([[4, 5], [5, 4], [5, 6], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7]])
    # grid.setup([4, 5], [4, 6], [5, 5], [5, 7], [6, 6], [6,7][,[4, 5], [4, 6], [5, 5], [5, 7], [6, 6], [6,7]])

    for _ in range(100):
        grid.show()
        grid.do_step()


if __name__ == "__main__":
    main()
