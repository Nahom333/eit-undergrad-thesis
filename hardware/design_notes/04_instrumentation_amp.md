# Instrumentation amplifier

## What this block must do
Amplify the difference between the two sensing electrodes and cancel what reaches both equally.

## My starting choice (from the proposal)
3-op-amp differential configuration using NE5532, target CMRR above 80 dB.

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
- Resistor matching and how it limits CMRR in practice (0.1 percent parts cannot give the datasheet CMRR on their own).
- Input bias and offset: do they matter after the JFET buffers?
