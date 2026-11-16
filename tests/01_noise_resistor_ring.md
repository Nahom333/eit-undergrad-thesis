# Test 01: noise on the resistor ring (specific objective 2)

## Goal
Measure the scatter of repeated readings with no tank, only identical resistors.

## Setup
- 8 nodes in a ring, identical resistors between neighbours (you have 5 percent resistors; better to measure them with a multimeter and choose a closely matched set, and note their values here): TODO
- Drive frequency: TODO (open_questions.md #1)
- Current amplitude: TODO

## Procedure
1. Record N frames (N = TODO) with nothing changed.
2. Save to data/raw/ as test01_<date>_<run>.npy.
3. Run analysis/noise_analysis.py.

## Record
Mean, standard deviation and SNR for every one of the 40 readings. Worst, median, best.

## Decision
Noise limit written before the test: TODO
Result: pass / fail
If fail: JLCPCB boards (decision_log.md).

## Notes / problems
TODO
