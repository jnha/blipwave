
import numpy as np
from scipy.io.wavfile import write

from blipwave import RATE

def to16bit(sound):
    """
    Convert a floating point sound clip to 16 bit with randomized rounding
    """
    return np.int16(sound*(2**15-1) + np.random.rand(len(sound)))
    
def write16bit(filename, sound, rate=RATE):
    """
    Write a floating point sound clip to a 16 bit .wav format
    """
    write(filename, rate, to16bit(sound))
