"""
Tools for creating and manipulating wavefunctions
"""

def shape(wave, freq, phase, amp, *args, **kargs):
    """
    Sets a wave's frequency, phase, and amplitude

    Args:
        wave: A sinusoid-like wave function
        freq: The frequency to set (in Hz)
        phase: The phase offset (in fractions of a cycle)
        amp: The amplitude (fraction of 1)

    Returns:
        The wave function with the set freqency, phase, and amplitude
    """
    return lambda t: amp * wave(2*pi*(freq*t + phase), *args, **kargs)

