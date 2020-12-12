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
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def start(self):
        print(self.color)
        pixels = np.tile(0, (3, 30))
        pixels[0, :30]=self.color[0]
        pixels[1, :30]=self.color[1]
        pixels[2, :30]=self.color[2]
        pixels = np.clip(pixels, 0, 255).astype(int)
        _prev_pixels = np.tile(0, (3, 30))
        MAX_PIXELS_PER_PACKET = 126
        # Pixel indices
        idx = range(pixels.shape[1])
        idx = [i for i in idx if not np.array_equal(pixels[:, i], _prev_pixels[:, i])]
        n_packets = len(idx) // MAX_PIXELS_PER_PACKET + 1
        idx = np.array_split(idx, n_packets)
        for packet_indices in idx:
            m = []
            for i in packet_indices:
                m.append(i)  # Index of pixel to change
                m.append(pixels[0][i])  # Pixel red value
                m.append(pixels[1][i])  # Pixel green value
                m.append(pixels[2][i])  # Pixel blue value
            m = bytes(m)
            self.socket.sendto(m, ('192.168.1.150', 7777))
        

    def kill(self):
        pass
