import time
import pygame

"""
	The Loop class.
	-----------------------------
	The main loop of the simulation.
"""
class Loop(object):

    """
        Constructor.
    """
    def __init__(self, configuration, screen, event):
        self.done = True
        self.configuration = configuration
        self.screen = screen
        self.event = event

    """
        Start the main loop.
    """
    def startLoop(self):
        self.done = False
        self.__loop()

    """
        Stop the main loop.
    """
    def stopLoop(self):
        self.done = True

    """
        The main loop.
    """
    def __loop(self):
        while self.done == False:

            self.__listenForEvents()

            self.screen.fill(self.configuration["COLOURS"]["BLACK"])
            pygame.display.flip()


    """
        Listen for events.
    """
    def __listenForEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stopLoop()
            if self._hasAction(event.type):
                self.fireAction(event.type)

    """
        Does this event has an action mapped to it?
    """
    def _hasAction(self, eventType):
        self.event.getMappedEvents();

