# Current source

## What this block must do
Push a steady AC current through the chosen electrode pair, whatever the load (the water plus electrode contact) is.

## My starting choice (from the proposal)
Modified Howland circuit using TL071CP with 0.1% precision resistors. The STM32 internal DAC makes the drive signal.

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
- What is the output resistance of my source? (It sets how constant the current really is.)
- What is the largest load it can drive before the op-amp runs out of voltage?
- Does the CD4051 on-resistance sit inside or outside the feedback loop? What does that change?
