import time

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
            screen.fill(BLACK)
            pygame.display.flip()
