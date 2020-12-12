from abc import ABCMeta, abstractmethod

class LightingType(object):
    """
    Base lighting type
    """
    def __init__(self):
        self.led_number = 30
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def kill(self):
        pass