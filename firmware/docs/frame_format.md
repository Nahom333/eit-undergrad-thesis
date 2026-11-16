# Frame format (decide, then do not change without logging it)

One frame = 8 injections x 5 readings = 40 values.
For each reading the laptop needs: which injection pair, which sensing pair, the raw samples (or an amplitude), and a frame number.

My format: TODO
(bytes, header, checksum, sample rate, samples per reading, USB mode)
