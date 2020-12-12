from lighting.lighting_type import LightingType
from lighting.static.static import StaticLighting
class Lighting():
    """
    Lighting settings applier class
    """
    def update(self, options):
        if options["type"] == "static":
            static = StaticLighting(options)
            static.start() 