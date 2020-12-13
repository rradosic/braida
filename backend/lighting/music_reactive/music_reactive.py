import subprocess
import os
import signal
from lighting.lighting_type import LightingType

class MusicReactiveLighting(LightingType):
    """
    Static lighting type
    """
    def __init__(self, options):
        super().__init__()
        
    
    def start(self):
        process = subprocess.Popen(["venv/bin/python","lighting/music_reactive/visualization.py"])
        self.pid = process.pid
        return True
    

    def kill(self):
        self.turn_off_leds()
        os.kill(self.pid, signal.SIGTERM)
        return True
