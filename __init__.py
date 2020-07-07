
RATE = 48000 # Default sample rate

from blipwave.sampling import sample
from blipwave.wavefunction import shape
from blipwave.envalope import adsr
from blipwave.sequence import sequence, clip
from blipwave.write_wave import write16bit
