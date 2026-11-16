# Host (laptop) software
capture.py reads frames from the STM32 and saves them in data/raw/.
demod.py does the synchronous demodulation: multiply by sine and cosine at the drive frequency, average, get amplitude and phase.
Both are skeletons with TODO markers.
