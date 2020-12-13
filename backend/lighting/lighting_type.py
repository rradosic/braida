from abc import ABCMeta, abstractmethod
from lighting.wireless_controller import WirelessController
import numpy as np

class LightingType( WirelessController):
    """
    Base lighting type
    """

    def __init__(self):
        from app import mongo
        global mongo
        settings = mongo.db.settings.find_one_or_404({"_id":1})
        self.leds_number = settings['ledSetup']['ledsNumber']

    def turn_off_leds(self):
        pixels = np.tile(0, (3, self.leds_number))
        self.send_packet(pixels)
    
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def kill():
        pass