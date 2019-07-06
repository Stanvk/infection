class Cell(object):


    """
      Initialise the Cell Object.

    """
    def __init__(self, row, column, age, type):
        self.row = row
        self.column = column
        self.age = age
        self.type = type

    def countNeighboursOfSameType(type):
        neighbours = [grid[row + 1][column], grid[row - 1][column], grid[row][column + 1], grid[row][column - 1],
                      grid[row + 1][column + 1], grid[row - 1][column - 1], grid[row - 1][column + 1],
                      grid[row + 1][column - 1]]

        return neighbours.count(type)