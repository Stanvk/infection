import pygame

class Simulation(object):

	#
	# Constructor.
	#
	def __init__(self):
		self.configuration = None
		self.screen = None


	#
	# Set Configuration variables.
	#
	def setConfiguration(self, configuration):
		self.configuration = configuration

	#
	# Start the simulation.
	#
	def start(self):
		self._initialisePygame()
		self.screen = self._initialiseGraphics(self.configuration["WIDTH"], self.configuration["HEIGHT"], self.configuration["MARGIN"])

	#
	# Initialise pygame.
	#
	def _initialisePygame(self):
		pygame.init()

	#
	# Initialise graphics and set window height, width and title.
	#
	def _initialiseGraphics(self, width, height, margin):
		window = [width, height]
		pygame.display.set_caption("Random Infection - by stanvk")

		return pygame.display.set_mode(window)

	def _initialiseGrid(self, numberOfRows, numberOfColumns):


