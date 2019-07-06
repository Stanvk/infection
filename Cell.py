class Cell(object):


    """
      Initialise the Cell Object.

    """
    def __init__(self, row, column):
        self.row = row;
        self.column = column;
        
    def anyNeighbouringCells(grid,row,column):
        if 