"""
Play sound clip
"""

import numpy as np
import simpleaudio
import random

from blipwave import RATE

def play(audio, rate=RATE):
    audio = np.int16(audio * (2**15 - 1) - random.random())
    p = simpleaudio.play_buffer(audio, 1, 2, RATE)
    p.wait_done()

