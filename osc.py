"""
Oscilators
"""

import numpy as np
from blipwave import RATE

def vco(frequencies, waveform, rate=48000):
    """
    Simulates a voltage controlled oscillator

    Args:
        frequencies: a numpy of instantaneous frequencies (in Hz) at each sample
        waveform: shape of the oscillation, any periodic function

    Returns:
        numpy array of waveform with varying frequency.
    """
    return waveform(2*np.pi * np.cumsum(frequencies/rate))

def lfo(freq, waveform, length, rate=48000):
    """
    Simulates a low frequency oscilator

    Args:
        freq: frequency of the oscillation
        waveform: form of the oscillation, a periodic function
        length: number of samples to output

    Returns:
        numpy array of waveform with constant frequency
    """
    return waveform(2 * np.pi * np.linspace(0, freq*length/rate, length))
