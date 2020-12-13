from lighting.lighting_type import LightingType
import numpy as np

class FlagLighting(LightingType):
    """
    Static lighting type
    """
    def __init__(self, options):
        super().__init__()
        self.country_code = options["typeOptions"]["country"]
        
    
    def start(self):
        pixels = self.get_pixels_for_country(self.country_code)
        print(pixels)
        self.send_packet(pixels)

        return True
    

    def kill(self):
        self.turn_off_leds()
        return True
    
    def get_pixels_for_country(self, country_code):
        pixels = np.tile(0, (3, 30))
        if country_code == "hr":
            leds_third = self.leds_number//3
            pixels[0, :leds_third] = 255
            pixels[0, leds_third:leds_third*2] = 255
            pixels[1, leds_third:leds_third*2] = 255
            pixels[2, leds_third:leds_third*2] = 255
            pixels[2, leds_third*2:leds_third*3] = 255

        else:
            pass
        return pixels
