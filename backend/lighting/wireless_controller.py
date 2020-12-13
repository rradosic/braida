import socket
import numpy as np

class WirelessController(object):
    def send_packet(self, pixels):
        esp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _prev_pixels = np.tile(266, (3, 30))
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
            esp_socket.sendto(m, ('192.168.1.150', 7777))