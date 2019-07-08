class Cell(object):

    """
      Initialise the Cell Object.
    """
    def __init__(self, row, column, age, type):
        self.row = row
        self.column = column
        self.age = age
        self.type = type

    """
        Count the neighbouring cells of a given type.
    """
    def countNeighboursOfType(self, type):
        neighbours = [grid[self.row + 1][self.column], grid[self.row - 1][self.column], grid[self.row][self.column + 1], grid[self.row][self.column - 1],
                      grid[self.row + 1][self.column + 1], grid[self.row - 1][self.column - 1], grid[self.row - 1][self.column + 1],
                      grid[self.row + 1][self.column - 1]]

        return neighbours.count(type)

    """
        Alters the type of the neighbouring cells to a given type.
    """
    def alterNeighbours(self, type):
        for i in range(-1,2):
            for j in range(-1,2):
                grid[self.row+i][self.column+j] = type

        return type;