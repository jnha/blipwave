"""
Preset synths
"""

import numpy as np
from scipy.signal import sawtooth

from blipwave import RATE, adsr, sample, shape

def tribase(freq, length, rate=RATE):
    envalope = adsr(1/32, 1/6, .30, length/2, length/2, rate=rate)
    sound = sample(shape(sawtooth, freq, 0, 1, 0.5), length, rate=rate)
    return envlope*sound[:len(envlope)]

def piano(wave, freq, length, *args, rate=RATE):
    envalope = adsr(1/20, 1/4, .95, max(1/20, length-1/20), 1/20, rate=rate)
    sound = sample(shape(wave, freq, 0, 1, *args), length, rate=rate)
    return envalope*sound[:len(envalope)]

