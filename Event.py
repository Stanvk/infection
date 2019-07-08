class Event(object):
    def __init__(self):
        self.mappedEvents([
            pygame.MOUSEBUTTONDOWN,
            pygame.KEYDOWN
        ])

    def getMappedEvents(self):
        return self.mappedEvents

    def countMappedEvent(self,event):
        return self.mappedEvents.count(event)