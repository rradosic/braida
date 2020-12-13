import os.path
import pickle

from lighting.lighting_type import LightingType
from lighting.static.static import StaticLighting
from lighting.flag.flag import FlagLighting
from lighting.music_reactive.music_reactive import MusicReactiveLighting

class Lighting():
    """
    Lighting settings applier class
    """

    def __init__(self):
        self.types = {'static': StaticLighting, 'flag': FlagLighting, 'music': MusicReactiveLighting}


    def update(self, options):
        if options["enabled"]:
            self.kill_current_lighting()

            lighting_type = options['type']

            instance = self.types[lighting_type](options)
            instance.start() 

            cache_file = open('lighting_cache', 'ab')
            pickle.dump(instance, cache_file)
            cache_file.close()
        else:
            self.kill_current_lighting()

    def kill_current_lighting(self):
        """
        Kills current lighting with data from cache
        """
        if os.path.isfile('lighting_cache'):
            cache_file = open('lighting_cache', 'rb')
            instance = pickle.load(cache_file)
            cache_file.close()
            if(issubclass(type(instance), LightingType)):
                instance.kill()
            
        