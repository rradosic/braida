from lighting.lighting_type import LightingType
import socket
import numpy as np

class StaticLighting(LightingType):
    """
    Static lighting type
    """
    def __init__(self, options):
        super().__init__()
        color_hex = options["typeOptions"]["color"]
        color = color_hex.lstrip("#")
        self.color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        
    
    def start(self):
        print(self.color)
        pixels = np.tile(0, (3, 30))
        pixels[0, :30]=self.color[0]
        pixels[1, :30]=self.color[1]
        pixels[2, :30]=self.color[2]
        pixels = np.clip(pixels, 0, 255).astype(int)
        
        self.send_packet(pixels)

        return True
    

    def kill(self):
        self.turn_off_leds()
        return True
