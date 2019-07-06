
import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = [(51, 51, 255), (0, 0, 255), (0, 0, 204), (0, 0, 153), (0, 0, 102)] # Five different blues, from light to dark.
RED = [(255, 51, 51), (255, 0, 0), (204, 0, 0), (153, 0, 0), (102, 0, 0)] # Five different reds, from light to dark.

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10
MARGIN = 1

numberOfRows = 70
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







# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [windowsWidth, windowsHeight]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Random Infection")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def determineColorAge(age):
    if (age<1):
        return 0
    elif(age<10):
        return 1
    elif(age<40):
        return 2
    elif(age<80):
        return 3
    elif(age<120):
        return 4

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

 
    # Set the screen background
    screen.fill(BLACK)

    for row in range(numberOfRows):
        for column in range(numberOfColumns):
            #Cell gets older..
            ageOfCells[row][column] = ageOfCells[row][column] + 1

            #Infect
            if row > 0 and column > 0 and row < (numberOfRows-1) and column < (numberOfColumns-1):
                #From white to red infection due neighbour red cell
                if grid[row+1][column] == 1 or grid[row-1][column] == 1 or grid[row][column+1] == 1 or grid[row][column-1] == 1:
                    if random.random() <= 0.05:
                        grid[row][column] = 1
                

    # Draw the grid
    for row in range(numberOfRows):
        for column in range(numberOfRows):
            # color = WHITE
            if grid[row][column] == 1:
                color = RED[determineColorAge(ageOfCells[row][column])]
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            # Go ahead and update the screen with what we've drawn.

    pygame.display.flip()            
 


# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()