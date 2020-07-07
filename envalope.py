"""
Envalopes
"""

import numpy as np

from blipwave import RATE

def adsr(attack, decay, sustain, release, length, rate=RATE):
    """
    Generates an adsr envalope for a note

    Args:
        attack: time until the note reaches its peak volume
        decay: time from the peak volume to the sustained volume
        sustain: the volume sustained while the note is held
        release: the time it takes for the note to dampen once released
        length: the length the note is held for
        rate: the sample rate    
    Returns:
        An array of samples of the adsr envalope
    """
    attack = int(rate*attack)
    decay = int(rate*decay)
    release = int(rate*release)
    length = int(rate*length)
    start = np.concatenate([np.linspace(0, 1, attack), np.linspace(1, sustain, decay), np.full(length, sustain)])
    envalope = start[0:length]
    return np.concatenate([envalope, np.linspace(envalope[-1], 0, release)])
