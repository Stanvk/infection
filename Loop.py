import time
import pygame

class Loop(object):
    def __init__(self, configuration, screen):
        self.done = True
        self.configuration = configuration
        self.screen = screen

    def startLoop(self):
        self.done = False
        self.__loop()

    def stopLoop(self):
        self.done = True

    def __loop(self):
        while self.done == False:

            self.__listenForEvents()

            self.screen.fill(self.configuration["COLOURS"]["BLACK"])
            pygame.display.flip()

    def __listenForEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stopLoop()