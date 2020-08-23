"""
Sequence

Tools for combining sounds into a single clip
"""

import numpy as np

from blipwave import RATE

def layer(sounds, offsets):
    """
    Layers a set of sound clips at given offsets

    Args:
        sounds: a list of sound clips
        offsets: a list of the number of samples to offset the corresponding sound clips

    Returns:
        A single clip with the sounds layered over each other
    """
    lengths = [len(sound) for sound in sounds]
    max_length = max(offset + length for offset, length in zip(offsets, lengths))
    clip = np.zeros(max_length)
    for sound, length, offset in zip(sounds, lengths, offsets):
        clip[offset : offset + length] += sound
    return clip

def sequence(sounds, times, rate=RATE):
    """
    Layers a set of sound clips in sequence

    Args:
        sounds: A list of sound clips
        times: A list of times between the start of clips in seconds

    Returns:
        A clip with the sound clips played in sequence
    """
    offsets = [0]
    for time in times:
        offsets.append(offsets[-1] + time * rate)
    offsets = [int(offset) for offset in offsets]
    return layer(sounds, offsets)

def clip(sound, length):
    """
    Cut or extend a sound clip to be the desired number of samples

    Args:
        sound: a sound clip
        length: the number of samples
    
    Returns:
        the sound clip with the length changed to the desired number of samples
    """
    if length <= len(sound):
        return sound[:length]
    return np.concatenate([sound, np.zeros(length - len(sound))])

def chord(synth, notes, length):
    try:
        return sum(synth(note, length) for note in notes)
    except TypeError:
        return synth(notes, length)

def chords(synth, notes, amp, lengths):
    return [chord(synth, n, l)*amp for n, l in zip(notes, lengths)]

