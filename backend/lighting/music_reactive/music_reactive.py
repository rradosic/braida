from lighting.lighting_type import LightingType
import socket
import numpy as np

class MusicReactiveLigting(LightingType):
    """
    Static lighting type
    """
    def __init__(self, options):
        super().__init__()
        
    
    def start(self):
        subprocess.run(["ls", "-l"], capture_output=True)
        return True
    

    def kill(self):
        self.turn_off_leds()
        return True
