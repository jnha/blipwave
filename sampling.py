"""
Tools for sampling waveforms
"""

import numpy as np

from blipwave import RATE

def sample(wave, length, rate=RATE):
    """
    Samples a waveform

    Args:
        wave: the waveform
        length: the length of time to sample in seconds
        rate: the sample rate in samples/second

    returns:
        An array of samples of the waveform
    """
    clip = np.linspace(0, length, int(length*rate))
    return wave(clip)
    
