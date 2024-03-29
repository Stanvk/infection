import pygame
import Cell
import Loop
import random


"""
	The Simulation class.
	-----------------------------
	This class is responsible for initiating all the 
	different components and starting the 'master loop'.
"""
class Simulation(object):

	"""
		Constructor.
	"""
	def __init__(self):
		self.configuration = None
		self.screen = None


	"""
		Set the configuration variables.
	"""
	def setConfiguration(self, configuration):
		self.configuration = configuration

	"""
		Start the simulation.
	"""
	def start(self):
		self._setGrid([])
		self._initialisePygame()
		self.screen = self._initialiseGraphics(self.configuration["WIDTH"], self.configuration["HEIGHT"], self.configuration["MARGIN"])
		self._initialiseGrid(self.configuration["ROWS"], self.configuration["COLUMNS"])

		self.loop = Loop.Loop(
			self.configuration,
			self.screen
		).startLoop()

	"""
		Get grid.
	"""
	def getGrid(self):
		return self.grid

	"""
		Set grid.
	"""
	def _setGrid(self, grid):
		self.grid = grid

	"""
		Initialise Pygame.
	"""
	def _initialisePygame(self):
		return pygame.init()

	"""
		Initialise graphics and set window height, width and title.
	"""
	def _initialiseGraphics(self, width, height, margin):
		pygame.display.set_caption("Random Infection - by stanvk")

		return pygame.display.set_mode([width, height])

	"""
		Initialise the Grid and initiate new cell objects for each cell.
	"""
	def _initialiseGrid(self, numberOfRows, numberOfColumns):
		for row in range(numberOfRows):
			self.grid.append([])
			for column in range(numberOfColumns):
				self.grid[row].append(0)
				self.grid[row][column] = Cell.Cell(row, column, 121, self.__getRandomType())

	"""
		Generates a pseudo-random type.
	"""
	def __getRandomType(self):
		return (0, 1)[random.random() <= 0.5]


