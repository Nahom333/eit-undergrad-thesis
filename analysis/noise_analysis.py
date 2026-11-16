"""Test 01: noise on the 8-node resistor ring. Skeleton."""
import numpy as np

# TODO: load frames, shape (n_frames, 40)
frames = None

def report(frames):
    mean = frames.mean(axis=0)          # per reading
    std = frames.std(axis=0, ddof=1)    # scatter of repeated readings
    snr_db = 20 * np.log10(np.abs(mean) / std)
    return mean, std, snr_db

# TODO: print worst, median and best reading; decide which one you quote in the report and why
# TODO: compare to the noise limit you wrote in docs/open_questions.md (#4)
