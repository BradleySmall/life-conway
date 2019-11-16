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
            return "\N{Full Block}"
        return " "

    def __repr__(self):
        """Representation."""
        if self.is_on():
            return "\N{Full Block}"
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

    # grid.setup([[4, 5], [5, 5], [6, 5], [7, 6], [7, 7], [7, 8]])
    # grid.setup([[4, 15], [5, 15], [6, 15], [7, 16], [7, 17], [7, 18]])
    # grid.setup([[14, 5], [15, 5], [16, 5], [17, 6], [17, 7], [17, 8]])
    # grid.setup([[14, 15], [15, 15], [16, 15], [17, 16], [17, 17], [17, 18]])

    # grid.setup([[4, 5], [5, 5], [6, 5], [7, 5]])
    # grid.setup([[4, 6], [5, 6], [6, 6], [7, 6]])
    # grid.setup([[4, 7], [5, 7], [6, 7], [7, 7]])
    # grid.setup([[4, 8], [5, 8], [6, 8], [7, 8]])
    # grid.setup([[4, 9], [5, 9], [6, 9], [7, 9]])
    # grid.setup([[4, 10], [5, 10], [6, 10], [7, 10]])
    # grid.setup([[4, 11], [5, 11], [6, 11], [7, 11]])
    # grid.setup([[4, 12], [5, 12], [6, 12], [7, 12]])

    # grid.setup([[4, 5], [5, 5], [6, 5], [7, 5], [8,5]])
    # grid.setup([[24, 25], [24, 26], [24, 27], [25, 25], [26, 26]])
    # grid.setup([[24, 25], [25, 26], [26, 24], [26, 25], [26, 26]])
    grid.setup([
               [5, 8], [5, 9], [5, 10], [5, 14], [5, 15], [5,16],
               [10, 8], [10, 9], [10, 10], [10, 14], [10, 15], [10,16],
               [12, 8], [12, 9], [12, 10], [12, 14], [12, 15], [12,16],
               [17, 8], [17, 9], [17, 10], [17, 14], [17, 15], [17,16],
               [7, 6], [7, 11], [7, 13], [7, 18],
               [8, 6], [8, 11], [8, 13], [8, 18],
               [9, 6], [9, 11], [9, 13], [9, 18],
               [13, 6], [13, 11], [13, 13], [13, 18],
               [14, 6], [14, 11], [14, 13], [14, 18],
               [15, 6], [15, 11], [15, 13], [15, 18]
               ])

    grid.show()
    for _ in range(200):
        grid.show()
        grid.do_step()


if __name__ == "__main__":
    main()
