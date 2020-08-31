"""
Filters
"""

import numpy as np
from scipy.signal import lfilter, butter, freqz

def lowpass(x, cutoff, rate=48000):
    """ Simple RC lowpass filter """
    alpha = 1/(rate/cutoff + 1)
    return lfilter([alpha], [1., alpha-1], x)

