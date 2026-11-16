"""Synchronous demodulation of one reading. Skeleton."""
import numpy as np

def demodulate(samples, fs, f_drive):
    """samples: 1D array covering a whole number of drive periods.
    Returns amplitude and phase at f_drive.
    TODO: check that you really sampled an integer number of periods, and say how in the report."""
    t = np.arange(len(samples)) / fs
    i = 2 * np.mean(samples * np.cos(2 * np.pi * f_drive * t))
    q = 2 * np.mean(samples * np.sin(2 * np.pi * f_drive * t))
    return np.hypot(i, q), np.arctan2(q, i)
