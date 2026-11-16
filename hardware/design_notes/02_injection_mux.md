# Injection multiplexer

## What this block must do
Choose which pair of electrodes carries the current.

## My starting choice (from the proposal)
Dual CD4051 (8:1) analog multiplexers with software settling delays.

## Requirements I set for it (numbers, with the reason)
TODO

## Calculation (component values, how I got them)
TODO

## Simulation (tool, file in hardware/, result)
TODO

## Built and measured (date, setup, results, file names in data/)
TODO

## Problems and what I changed
TODO

## Extra checks to do on this block
- On-resistance of the CD4051 and how it varies with signal level and supply.
- Charge injection / settling after a switch change: how long must I wait before reading?
- Channel-to-channel leakage when a channel is off.
