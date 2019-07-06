
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
BLUE = [(51, 51, 255), (0, 0, 255), (0, 0, 204), (0, 0, 153), (0, 0, 102)] # Five different blues, from light to dark.
RED = [(255, 51, 51), (255, 0, 0), (204, 0, 0), (153, 0, 0), (102, 0, 0)] # Five different reds, from light to dark.

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10
MARGIN = 1

numberOfRows = 76
numberOfColumns = numberOfRows

windowsWidth = (MARGIN+WIDTH)*numberOfColumns
windowsHeight = (MARGIN+HEIGHT)*numberOfColumns

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
ageOfCells = []
for row in range(numberOfRows):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(numberOfColumns):
        grid[row].append(0)  # Append a cell

for row in range(numberOfRows):
    # Add an empty array that will hold each cell
    # in this row
    ageOfCells.append([])
    for column in range(numberOfColumns):
        ageOfCells[row].append(0)  # Append a cell


#Blue is 0
#Red is 1

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [windowsWidth, windowsHeight]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Random Infection RED vs BLUE - by Stanvk")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Initial infection of the grid
for row in range(numberOfRows):
    for column in range(round(numberOfColumns)):
        if random.random() <= 0.5:
            grid[row][column] = 1

#Set the age of all cells at 121
for row in range(numberOfRows):
    for column in range(numberOfColumns):
        ageOfCells[row][column] = 121

#Count the neigbouring cells of the same type for a given cell.
def countNeighboursOfSameType(row, column, type):
    neighbours = [grid[row+1][column], grid[row-1][column], grid[row][column+1], grid[row][column-1], grid[row+1][column+1], grid[row-1][column-1]]

    return neighbours.count(type)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

 
    # Set the screen background
    screen.fill(BLACK)

    for row in range(numberOfRows):
        for column in range(numberOfColumns):

            statusBefore = grid[row][column]


            if row > 0 and column > 0 and row < (numberOfRows-1) and column < (numberOfColumns-1):

                #Infect
                if countNeighboursOfSameType(row, column, 1) != 0:
                    chanceOfInfection = 0.059*countNeighboursOfSameType(row, column, 1)
                    if random.random() <= chanceOfInfection:
                        grid[row][column] = 1

                #disinfect
                if countNeighboursOfSameType(row, column, 0) != 0:
                    chanceOfDisinfection = 0.05*countNeighboursOfSameType(row, column, 0);
                    if random.random() <= chanceOfDisinfection:
                        grid[row][column] = 0

            if statusBefore == grid[row][column]:
                ageOfCells[row][column] = ageOfCells[row][column] + 1
            elif statusBefore != grid[row][column]:
                ageOfCells[row][column] = 0

                

    # Draw the grid
    for row in range(numberOfRows):
        for column in range(numberOfRows):

            if grid[row][column] == 0:
                color = BLUE[0]
                if ageOfCells[row][column] < 30:
                    color = BLUE[1]
                elif ageOfCells[row][column] < 60:
                    color = BLUE[2]
                elif ageOfCells[row][column] < 90:
                    color = BLUE[3]
                elif ageOfCells[row][column] > 120:
                    color = BLUE[4]

            if grid[row][column] == 1:
                color = RED[0]
                if ageOfCells[row][column] < 30:
                    color = RED[1]
                elif ageOfCells[row][column] < 60:
                    color = RED[2]
                elif ageOfCells[row][column] < 90:
                    color = RED[3]
                elif ageOfCells[row][column] > 120:
                    color = RED[4]



            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])


    pygame.display.flip()
 

pygame.quit()