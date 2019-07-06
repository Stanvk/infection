class Simulation(object):

	def __init__(self):
		self.configuration = None
		self.screen = None


	#
	#	Set Configuration variables.
	#
	def setConfiguration(self, configuration):
		self.configuration = configuration

	#
	# Start the simulation.
	#
	def start(self):
		initialisePygame()
		self.screen = _initialiseGraphics(self.configuration["WIDTH"], self.configuration["HEIGHT"], self.configuration["MARGIN"])

	#
	# Initialise pygame.
	#
	def _initialisePygame(self):
		pygame.init()

	#
	# Initialise graphics and set window height, width and title.
	#
	def _initialiseGraphics(self, width, height, margin):
		window = [windowsWidth, windowsHeight]
		screen = pygame.display.set_mode(window)
		pygame.display.set_caption("Random Infection - by stanvk")

		return screen